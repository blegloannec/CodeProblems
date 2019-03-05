#!/usr/bin/env python3

from collections import defaultdict

S = 10

Used = set()
def backtrack(p=0):
    if p==len(P):
        return True
    i,j,di,dj,l = P[p]
    known = [k for k in range(l) if G[i+k*di][j+k*dj]!='-']
    for w in W[l]:
        if w not in Used and all(G[i+k*di][j+k*dj]==w[k] for k in known):
            Used.add(w)
            for k in range(l):
                G[i+k*di][j+k*dj] = w[k]
            if backtrack(p+1):
                return True
            Used.remove(w)
    return False

if __name__=='__main__':
    G = [list(input()) for _ in range(S)]
    W0 = input().split(';')
    W = defaultdict(list)
    for w in W0:
        W[len(w)].append(w)
    P = []
    for i in range(S):
        j = 0
        while j<S:
            if G[i][j]=='-':
                j0 = j
                while j<S and G[i][j]=='-':
                    j += 1
                w = j-j0
                if w>1:
                    P.append((i,j0,0,1,w))
            j += 1
    for j in range(S):
        i = 0
        while i<S:
            if G[i][j]=='-':
                i0 = i
                while i<S and G[i][j]=='-':
                    i += 1
                h = i-i0
                if h>1:
                    P.append((i0,j,1,0,h))
            i += 1
    assert backtrack()
    print('\n'.join(''.join(L) for L in G))
