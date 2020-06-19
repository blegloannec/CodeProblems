#!/usr/bin/env python3

import sys
input = sys.stdin.readline

INF = 1<<30

def dfs_dp(u, u0=-1):
    res = 0
    for v,w in T[u]:
        if v!=u0:
            res += min(w, dfs_dp(v, u))
    if res==0:  # leaf
        res = INF
    return res

def main():
    global N,T
    while True:
        try:
            N,c = map(int, input().split())
        except ValueError:
            break
        c -= 1
        T = [[] for _ in range(N)]
        for _ in range(N-1):
            u,v,w = map(int, input().split())
            u -= 1
            v -= 1
            T[u].append((v,w))
            T[v].append((u,w))
        print(dfs_dp(c))

main()
