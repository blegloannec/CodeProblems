#!/usr/bin/env python3

# The graph is a DAG, easy DP

n = int(input())
G = [None]*n
M = [0]*(n+1)
lint = lambda x: n if x=='E' else int(x)
for _ in range(n):
    u,m,v1,v2 = map(lint,input().split())
    M[u] = m
    G[u] = (v1,v2)

C = [None]*(n+1)
C[n] = 0
def dp(u=0):
    if C[u]==None:
        C[u] = M[u] + max(dp(v) for v in G[u])
    return C[u]

print(dp())
