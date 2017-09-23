#!/usr/bin/env pypy

import rosalib

def global_score(u,v):
    m,n = len(u),len(v)
    T = [[float('-inf')]*(n+1) for _ in xrange(m+1)]
    T[0][0] = 0
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i>0 and j>0:
                T[i][j] = max(T[i][j], T[i-1][j-1]+(1 if u[i-1]==v[j-1] else -1))
            if i>0:
                T[i][j] = max(T[i][j], T[i-1][j]-1)
            if j>0:
                T[i][j] = max(T[i][j], T[i][j-1]-1)
    return T

def align_matrix(A,B):
    T = global_score(A,B)
    Tinv = global_score(A[::-1],B[::-1])
    m,n = len(A),len(B)
    M = [[0]*n for _ in xrange(m)]
    for i in range(m):
        for j in range(n):
            M[i][j] = (1 if A[i]==B[j] else -1) + T[i][j] + Tinv[m-(i+1)][n-(j+1)]
    return T[m][n],M

def main():
    A,B = (S for _,S in rosalib.parse_fasta())
    s,M = align_matrix(A,B)
    print(s)
    print(sum(sum(L) for L in M))

main()
