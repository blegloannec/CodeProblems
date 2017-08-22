#!/usr/bin/env python3

import rosalib

def Levenstein(u,v):
    m,n = len(u),len(v)
    T = [[max(i,j) for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            T[i][j] = min(T[i-1][j]+1,T[i][j-1]+1,T[i-1][j-1]+int(u[i-1]!=v[j-1]))
    return T[m][n]

L = rosalib.parse_fasta()
print(Levenstein(L[0][1],L[1][1]))
