#!/usr/bin/env python3

N = 26

def dfs_cycle(Graph, Open, Closed, u):
    if not Closed[u]:
        if Open[u]:
            return True
        Open[u] = True
        for v in Graph[u]:
            if dfs_cycle(Graph, Open, Closed, v):
                return True
        Closed[u] = True
    return False

def main():
    m = int(input())
    G = [[] for _ in range(N)]
    for _ in range(m):
        u,d,v = input().split()
        u = ord(u)-ord('A')
        v = ord(v)-ord('A')
        if d=='<': G[u].append(v)
        else:      G[v].append(u)
    O = [False]*N
    C = [False]*N
    cycle = any(dfs_cycle(G, O, C, u) for u in range(N))
    print('contradiction' if cycle else 'consistent')

main()
