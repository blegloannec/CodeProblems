#!/usr/bin/env python3

from collections import deque

W = int(input())
N = int(input())
C = [int(input()) for _ in range(N)]

def succ(s):
    s = list(s)
    for i in range(N):
        if s[i]<C[i]:           # fill
            t = s[:]
            t[i] = C[i]
            yield tuple(t)
        if s[i]>0:              # empty
            t = s[:]
            t[i] = 0
            yield tuple(t)
            for j in range(N):  # pour
                if j!=i and s[j]<C[j]:
                    w = min(s[i],C[j]-s[j])
                    t = s[:]
                    t[i] -= w
                    t[j] += w
                    yield tuple(t)

def bfs():
    s0 = tuple([0]*N)
    D = {s0:0}
    Q = deque([s0])
    while Q:
        s = Q.popleft()
        if W in s:
            return D[s]
        for t in succ(s):
            if t not in D:
                D[t] = D[s]+1
                Q.append(t)

print(bfs())
