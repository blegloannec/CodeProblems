#!/usr/bin/env python3

import rosalib

def pdist(A,B):
    assert(len(A)==len(B))
    return sum(int(A[i]!=B[i]) for i in range(len(A)))/len(A)

def main():
    L = rosalib.parse_fasta()
    for i in range(len(L)):
        print(' '.join(str(pdist(L[i][1],L[j][1])) for j in range(len(L))))

main()
