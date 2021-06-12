#!/usr/bin/env python3

from collections import deque

def main():
    lenP = int(input())
    P0 = input()
    lenS = int(input())
    S = input()
    H,W = map(int, input().split())
    for _ in range(H):
        P = deque(P0)
        si = d0 = 0
        L = []
        for d in map(int, input()):
            dd, d0 = d-d0, d
            if dd<0:
                si, si0 = si-dd, si
                for i in range(si-1, si0-1, -1):
                    P.appendleft(S[i])
            else:
                for _ in range(dd):
                    P.popleft()
            L.append(P[0])
            P.rotate(-1)
        print(''.join(L))

main()
