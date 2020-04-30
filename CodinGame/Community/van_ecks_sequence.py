#!/usr/bin/env python3

u = int(input())
N = int(input())

Seen = {}
for t in range(1,N):
    t0 = Seen.get(u,t)
    Seen[u] = t
    u = t-t0
print(u)
