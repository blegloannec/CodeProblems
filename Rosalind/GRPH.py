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

def edge(A,B):
    return A[-3:]==B[:3] and A!=B

def main():
    J = parse_fasta()
    for i in range(len(J)):
        for j in range(len(J)):
            if edge(J[i][1],J[j][1]):
                print(J[i][0],J[j][0])

main()
