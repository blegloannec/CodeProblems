#!/usr/bin/env python3

from heapq import *

JE = 'Jane Eyre'

def read_books(Current, Pending):
    heapify(Current)
    Pending.sort(reverse=True)
    t = 0
    while Current:
        while Pending and Pending[-1][0]<=t:
            _,title,dt = Pending.pop()
            heappush(Current, (title,dt))
        title, dt = heappop(Current)
        t += dt
        if title==JE:
            break
    return t

def main():
    N,M,K = map(int,input().split())
    Current = [(JE,K)]
    for _ in range(N):
        I = input()
        i = I.rindex('"')
        title = I[1:i]
        dt = int(I[i+2:])
        Current.append((title,dt))
    Pending = []
    for _ in range(M):
        I = input()
        i, j = I.index('"'), I.rindex('"')
        title = I[i+1:j]
        t0 = int(I[:i-1])
        dt = int(I[j+2:])
        Pending.append((t0,title,dt))
    print(read_books(Current, Pending))

main()
