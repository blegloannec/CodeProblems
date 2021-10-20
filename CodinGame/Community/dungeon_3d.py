#!/usr/bin/env python3

from collections import deque

def bfs(u0, u1):
    Dist = [[[-1]*C for _ in range(R)] for _ in range(L)]
    l0,r0,c0 = u0
    Dist[l0][r0][c0] = 0
    Q = deque([(l0,r0,c0)])
    while Q:
        l,r,c = u = Q.popleft()
        if u==u1:
            return Dist[l][r][c]
        for vl,vr,vc in ((l-1,r,c),(l+1,r,c),(l,r-1,c),(l,r+1,c),(l,r,c-1),(l,r,c+1)):
            if 0<=vl<L and 0<=vr<R and 0<=vc<C and Map[vl][vr][vc]!='#' and Dist[vl][vr][vc]<0:
                Dist[vl][vr][vc] = Dist[l][r][c] + 1
                Q.append((vl,vr,vc))
    return 'NO PATH'

def main():
    global L,R,C, Map
    L,R,C = map(int, input().split())
    input()
    Map = []
    for l in range(L):
        input()
        Map.append([input() for _ in range(R)])
        for r in range(R):
            for c in range(C):
                if Map[l][r][c]=='A':
                    u0 = (l,r,c)
                elif Map[l][r][c]=='S':
                    u1 = (l,r,c)
    print(bfs(u0, u1))

main()
