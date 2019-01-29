#!/usr/bin/env python3

from collections import defaultdict

def compte(X):
    full = (1<<len(X))-1
    E = [defaultdict(lambda: float('inf')) for _ in range(full+1)]
    for i in range(len(X)):
        E[1<<i][X[i]] = 0
    for S in range(3,full+1):
        if S&(S-1):  # S not a power of 2
            for L in range(1,S):
                if L&S==L:
                    R = S^L
                    for l in E[L]:
                        E[S][l] = min(E[S][l],E[L][l])
                        for r in E[R]:
                            d = 1+E[L][l]+E[R][r]
                            if L<R:  # to avoid duplicate calculations
                                E[S][l+r] = min(E[S][l+r],d)
                                E[S][l*r] = min(E[S][l*r],d)
                            if l>r:
                                E[S][l-r] = min(E[S][l-r],d)
                            if r!=0 and l%r==0:  # integer div
                                E[S][l//r] = min(E[S][l//r],d)
    return E[full]

if __name__=='__main__':
    v = int(input())
    X = list(map(int,input().split()))
    E = compte(X)
    if v in E:
        print('POSSIBLE')
        print(E[v])
    else:
        print('IMPOSSIBLE')
        print(min(abs(w-v) for w in E))
