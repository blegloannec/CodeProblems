#!/usr/bin/env python3

import sys
from collections import deque

# rough upper bound for the time window of junctions
# without a time window
inf = 500

def bfs():
    Q = deque([(s,0)])
    visited = set([(s,0)])
    while Q:
        u,du = Q.popleft()
        if u==t:
            return True
        for (v,d) in G[u]:
            dv = du+d
            if (v,dv) not in visited and TW[v][0]<=dv<=TW[v][1]:
                visited.add((v,dv))
                Q.append((v,dv))
    return False

def main():
    global s,t,TW,G
    n,m,ntw = map(int,sys.stdin.readline().split())
    s,t = map(int,sys.stdin.readline().split())
    TW = [(0,inf)]*n
    for _ in range(ntw):
        v,b,e = map(int,sys.stdin.readline().split())
        TW[v] = (b,e)
    G = [[] for _ in range(n)]
    for _ in range(m):
        u,v,d = map(int,sys.stdin.readline().split())
        G[u].append((v,d))
    print('true' if bfs() else 'false')

main()
