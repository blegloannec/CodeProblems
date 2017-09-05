#!/usr/bin/env python3

from math import log10

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

# code d'evolution de WFMD
def evol0(N,m,g):
    prob0 = []
    P = [0]*(2*N+1)
    P[m] = 1
    for _ in range(g):
        P1 = [0]*(2*N+1)
        for m0 in range(2*N+1):
            p = m0/(2*N)
            for m1 in range(2*N+1):
                P1[m1] += P[m0] * binom(2*N,m1) * p**m1 * (1-p)**(2*N-m1)
        P = P1
        prob0.append(P[0])  # proba d'avoir 0 allele a la generation courante
    return prob0

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    P = [evol0(n,a,m) for a in A]
    for i in range(m):
        print(' '.join(str(log10(P[k][i])) for k in range(len(A))))

main()
