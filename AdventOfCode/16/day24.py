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

def heap(n,A):
    if n==1:
        yield A
    else:
        for i in xrange(n-1):
            for B in heap(n-1,A):
                yield B
            if n%2==0:
                A[i],A[n-1] = A[n-1],A[i]
            else:
                A[0],A[n-1] = A[n-1],A[0]
        for B in heap(n-1,A):
            yield B

d1,d2 = float('inf'),float('inf')
# trying all permutations, it's a TSP anyway!
for P in heap(N-1,range(1,N)):
    d0 = dists[0][V[P[0]]]
    for i in xrange(len(P)-1):
        d0 += dists[P[i]][V[P[i+1]]]
    d1 = min(d1,d0)
    # going back to 0 for part two
    d0 += dists[P[-1]][V[0]]
    d2 = min(d2,d0)
print d1,d2
