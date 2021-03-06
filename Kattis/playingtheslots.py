#!/usr/bin/env python3

# see also blowingcandles.py for a harder variant

from math import sqrt

dist = lambda x,y: sqrt(x*x + y*y)

def main():
    N = int(input())
    P = [tuple(map(float,input().split())) for _ in range(N)]
    min_diam = float('inf')
    # naive O(N^2) search is good enough here
    # O(N) is possible by a rotating-calipers-like approach
    # (between an edge and a vertex, see blowingcandles.py)
    for i in range(N):
        j = (i+1)%N
        x0, y0 = P[j][0]-P[i][0], P[j][1]-P[i][1]
        n = dist(x0, y0)
        nx, ny = -y0/n, x0/n
        d = 0.
        for k in range(N):
            if k!=i and k!=j:
                x1, y1 = P[k][0]-P[i][0], P[k][1]-P[i][1]
                dot = abs(x1*nx + y1*ny)
                d = max(d, dot)
        min_diam = min(min_diam, d)
    print(min_diam)

main()
