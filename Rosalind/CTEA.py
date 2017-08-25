#!/usr/bin/env python3

import rosalib

# NB: the statement explains "Why Are We Counting Modulo 134,217,727?
#     (...) however, if we count modulo a large prime number"
# yet 2^27-1 = 134217727 is not prime... (-_-)

def Levenstein_align(u,v):
    m,n = len(u),len(v)
    T = [[max(i,j) for j in range(n+1)] for i in range(m+1)]
    Nb = [[int(i==0 or j==0) for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            T[i][j] = min(T[i-1][j]+1,T[i][j-1]+1,T[i-1][j-1]+int(u[i-1]!=v[j-1]))
            if T[i-1][j]+1==T[i][j]:
                Nb[i][j] += Nb[i-1][j]
            if T[i][j-1]+1==T[i][j]:
                Nb[i][j] += Nb[i][j-1]
            if T[i-1][j-1]+int(u[i-1]!=v[j-1])==T[i][j]:
                Nb[i][j] += Nb[i-1][j-1]
    return (T[m][n],Nb[m][n])

L = rosalib.parse_fasta()
_,cpt = Levenstein_align(L[0][1],L[1][1])
print(cpt % (2**27-1))
