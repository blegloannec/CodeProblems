#!/usr/bin/env pypy

# O(n^2) DP with inputs of size 10^4
# runs in ~9s with pypy (using about ~3GB memory, though this could
# be greatly optimized, as pred is implemented expensively here,
# and is of course not even actually needed to climb back)

import rosalib

def semi_global_score(u,v):
    m,n = len(u),len(v)
    T = [[float('-inf') for j in xrange(n+1)] for i in xrange(m+1)]
    pred = [[None]*(n+1) for _ in range(m+1)]
    T[0][0] = 0
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i>0 and j>0:
                s = T[i-1][j-1] + (1 if u[i-1]==v[j-1] else -1)
                if s>T[i][j]:
                    T[i][j] = s
                    pred[i][j] = (i-1,j-1)
            if i>0:
                s = T[i-1][j] - int(0<j<n)
                if s>T[i][j]:
                    T[i][j] = s
                    pred[i][j] = (i-1,j)
            if j>0:
                s = T[i][j-1] - int(0<i<m)
                if s>T[i][j]:
                    T[i][j] = s
                    pred[i][j] = (i,j-1)
    i,j = m,n
    Su,Sv = [],[]
    while pred[i][j]:
        pi,pj = pred[i][j]
        Su.append(u[i-1] if pi<i else '-')
        Sv.append(v[j-1] if pj<j else '-')
        i,j = pi,pj
    return T[m][n],''.join(reversed(Su)),''.join(reversed(Sv))

def main():
    A,B = tuple(S for _,S in rosalib.parse_fasta())
    M,SA,SB = semi_global_score(A,B)
    print(M)
    print(SA)
    print(SB)

main()
