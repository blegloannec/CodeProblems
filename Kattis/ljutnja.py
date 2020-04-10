#!/usr/bin/env python3

# greedy approach: always reduce the largest value

from itertools import groupby

def main():
    M, N = map(int, input().split())
    A = sorted(int(input()) for _ in range(N))
    C = [(0,0)] + [(v,len(list(l))) for v,l in groupby(A)]
    while M:
        v1,c1 = C.pop()
        v0,c0 = C[-1]
        req = (v1-v0)*c1
        if req<=M:
            M -= req
            C.pop()
            C.append((v0,c0+c1))
        else:
            q,r = divmod(M, c1)
            C.append((v1-q,c1-r))
            C.append((v1-q-1,r))
            M = 0
    print(sum(c*v*v for v,c in C) % (1<<64))  # bullshit mod required

main()
