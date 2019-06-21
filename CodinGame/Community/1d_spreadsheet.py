#!/usr/bin/env python3

# see also ACM-ICPC UVa 196 - Spreadsheet

from operator import add, sub, mul
Op = {'ADD': add, 'SUB': sub, 'MULT': mul, 'VALUE': (lambda x,_: x)}

# O(N) approach through topological sort
def topo_spread():
    T = [0]*N
    val = lambda X: None if X=='_' else T[int(X[1:])] if X[0]=='$' else int(X)
    PredCnt = [0]*N
    Succ = [[] for _ in range(N)]
    Q = []
    for i in range(N):
        Pred = []
        for X in S[i][1:]:
            if X[0]=='$':
                Pred.append(int(X[1:]))
        PredCnt[i] = len(Pred)
        for j in Pred:
            Succ[j].append(i)
        if PredCnt[i]==0:
            Q.append(i)
    while Q:  # topo sort
        i = Q.pop()
        O,A,B = S[i]
        T[i] = Op[O](val(A),val(B))
        for j in Succ[i]:
            PredCnt[j] -= 1
            if PredCnt[j]==0:
                Q.append(j)
    return T

if __name__=='__main__':
    N = int(input())
    S = [input().split() for _ in range(N)]
    T = topo_spread()
    print('\n'.join(map(str,T)))
