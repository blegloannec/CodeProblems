#!/usr/bin/env python

import sys
from collections import deque

G = [L.strip() for L in sys.stdin.readlines()]
X,Y = len(G),len(G[0])
V = {}
for i in xrange(X):
    for j in xrange(Y):
        if ord('0')<=ord(G[i][j])<=ord('9'):
            V[ord(G[i][j])-ord('0')] = (i,j)
N = len(V)

# and yet another bfs!...
def bfs(start):
    Q = deque([start])
    dist = {start:0}
    while Q:
        x,y = Q.popleft()
        d = dist[x,y]
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=vx<X and 0<=vy<Y and G[vx][vy]!='#':
                if (vx,vy) not in dist:
                    dist[vx,vy] = d+1
                    Q.append((vx,vy))
    return dist

# min dists from each point of interest
dists = [bfs(V[i]) for i in xrange(N)]

def enum(S):
    i = 0
    while S>0:
        if S&1:
            yield i
        S >>= 1
        i += 1

# bitmask-based Held-Karp for the TSP
memo = {}
def D(S,c):
    if (S,c) in memo:
        return memo[S,c]
    if S==0:
        res = dists[0][V[c]]
    else:
        res = min(D(S^(1<<x),x)+dists[x][V[c]] for x in enum(S))
    memo[S,c] = res
    return res

def TSP(n):
    S = ((1<<n)-1)^1 # all points of interests (0 excluded)
    res1 = min(D(S^(1<<x),x) for x in xrange(1,n))
    # going back to 0 for part two
    res2 = min(D(S^(1<<x),x)+dists[x][V[0]] for x in xrange(1,n))
    return res1,res2

print TSP(N)
