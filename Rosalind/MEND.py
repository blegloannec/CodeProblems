#!/usr/bin/env python3

import rosalib

Num = {'aa':0,'Aa':1,'AA':2}
# mating matrix
MM = [[(1,0,0),    (1/2,1/2,0),  (0,1,0)],
      [(1/2,1/2,0),(1/4,1/2,1/4),(0,1/2,1/2)],
      [(0,1,0),    (0,1/2,1/2),  (0,0,1)]]

def dfs_prob(T,u):
    if u[0]!='@':
        return tuple(int(Num[u]==i) for i in range(3))
    assert(len(T[u])==2)
    A,B = dfs_prob(T,T[u][0]),dfs_prob(T,T[u][1])
    P = [0]*3
    for i in range(3):
        for j in range(3):
            for k in range(3):
                P[k] += A[i]*B[j]*MM[i][j][k]
    return tuple(P)

def main():
    T = {}
    R = rosalib.parse_newick(input(),T,False)
    P = dfs_prob(T,R)
    # l'enonce les veut dans l'ordre AA,Aa,aa
    print(' '.join(map(str,reversed(P))))

main()
