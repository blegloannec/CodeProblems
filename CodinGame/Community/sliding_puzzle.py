#!/usr/bin/env python3

from collections import deque

def bfs(u0,final):
    dist = {u0:0}
    Q = deque([u0])
    while Q:
        u = Q.popleft()
        if u==final:
            return dist[u]
        i = u.find('.')
        x,y = i//W,i%W
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=vx<H and 0<=vy<W:
                v = list(u)
                v[i],v[vx*W+vy] = v[vx*W+vy],v[i]
                v = ''.join(v)
                if v not in dist:
                    dist[v] = dist[u]+1
                    Q.append(v)

def main():
    global W,H
    H,W = map(int,input().split())
    G = []
    for _ in range(H):
        G += input().split()
    G = ''.join(G)
    final = ''.join(list(map(str,range(1,W*H)))+['.'])
    print(bfs(G,final))

main()
