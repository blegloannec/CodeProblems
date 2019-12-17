#!/usr/bin/env python3

from collections import defaultdict

# 2D hex grid as the projection of 3D discrete plane x+y+z = 0
# see also http://oeis.org/A002898

V = ((0,1,-1),(0,-1,1),(1,0,-1),(-1,0,1),(-1,1,0),(1,-1,0))

def dp(N=15):
    S = [defaultdict(int) for _ in range(N)]
    S[0][0,0,0] = 1
    for n in range(1,N):
        for (x,y,z),c in S[n-1].items():
            for dx,dy,dz in V:
                S[n][x+dx,y+dy,z+dz] += c
    return [s[0,0,0] for s in S]

def main():
    DP = dp()
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(DP[n])

main()
