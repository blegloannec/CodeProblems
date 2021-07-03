#!/usr/bin/env python3

from collections import defaultdict, deque

def bfs(u0, uf):
    Q = deque([u0])
    Pred = {u0: None}
    while True:
        u = Q.popleft()
        if u==uf: break
        for v in G[u]:
            if v not in Pred:
                Pred[v] = u
                Q.append(v)
    Path = []
    u = uf
    while u is not None:
        Path.append(u)
        u = Pred[u]
    Path.reverse()
    return Path

def main():
    global G
    u0 = input()
    uf = input()
    n = int(input())
    G = defaultdict(list)
    for _ in range(n):
        u,v = input().split()
        G[u].append(v)
        G[v].append(u)
    Path = bfs(u0, uf)
    print(' > '.join(Path))

main()
