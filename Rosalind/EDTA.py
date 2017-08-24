#!/usr/bin/env python3

import rosalib

def Levenstein_align(u,v):
    m,n = len(u),len(v)
    T = [[max(i,j) for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            T[i][j] = min(T[i-1][j]+1,T[i][j-1]+1,T[i-1][j-1]+int(u[i-1]!=v[j-1]))
    # construction de l'alignement
    i,j = m,n
    U,V = [],[]
    while i>0 or j>0:
        if i==0 or T[i][j]==T[i][j-1]+1:
            U.append('-')
            V.append(v[j-1])
            j -= 1
        elif j==0 or T[i][j]==T[i-1][j]+1:
            U.append(u[i-1])
            V.append('-')
            i -= 1
        else:
            U.append(u[i-1])
            V.append(v[j-1])
            i -= 1
            j -= 1
    return (T[m][n],''.join(reversed(U)),''.join(reversed(V)))

L = rosalib.parse_fasta()
d,S,T = Levenstein_align(L[0][1],L[1][1])
print(d)
print(S)
print(T)
