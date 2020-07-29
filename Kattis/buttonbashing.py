#!/usr/bin/env python3

from collections import deque
M = 3600

def bfs(B, tf):
    T = [None]*(M+1)
    T[0] = 0
    Q = deque([0])
    while Q:
        t = Q.popleft()
        if t==tf:
            break
        for b in B:
            t1 = max(0, min(t+b, M))
            if T[t1] is None:
                T[t1] = T[t]+1
                Q.append(t1)
    # as there is at least one b>0, we know T[M] is not None
    for t in range(tf, M+1):
        if T[t] is not None:
            return (T[t], t-tf)

def main():
    C = int(input())
    for _ in range(C):
        N,T = map(int, input().split())
        B = tuple(map(int, input().split()))
        print(*bfs(B, T))

main()
