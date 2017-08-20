#!/usr/bin/env python3

import sys

def parse_fasta():
    I = sys.stdin.readlines()
    J = []
    i = 0
    while i<len(I):
        N = I[i].strip()[1:]
        i += 1
        A = [I[i].strip()]
        i += 1
        while i<len(I) and I[i][0]!='>':
            A.append(I[i].strip())
            i += 1
        J.append((N,''.join(A)))
    return J

def main():
    D = {'A':0,'C':1,'G':2,'T':3}
    Dinv = 'ACGT'
    L = parse_fasta()
    N = len(L[0][1])
    C = [[0]*N for _ in range(4)]
    for _,DNA in L:
        for i in range(N):
           C[D[DNA[i]]][i] += 1
    cons = ''.join(Dinv[max((C[a][i],a) for a in range(4))[1]] for i in range(N))
    print(cons)
    for i in range(4):
        print(Dinv[i]+':',' '.join(map(str,C[i])))

main()
