#!/usr/bin/env pypy

# similar to SMGB except it is not symmetric:
# gaps are only free at the beginning/end of v

import rosalib

def fitting_score(u,v):
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
                s = T[i][j-1] - 1
                if s>T[i][j]:
                    T[i][j] = s
                    pred[i][j] = (i,j-1)
    i,j = m,n
    Su,Sv = [],[]
    while j>0:              # to remove the prefix of u
        pi,pj = pred[i][j]
        if Sv or pj<j:      # to remove the suffix of u
            Su.append(u[i-1] if pi<i else '-')
            Sv.append(v[j-1] if pj<j else '-')
        i,j = pi,pj
    return T[m][n],''.join(reversed(Su)),''.join(reversed(Sv))

def main():
    A,B = (S for _,S in rosalib.parse_fasta())
    M,SA,SB = fitting_score(A,B)
    print(M)
    print(SA)
    print(SB)

main()
