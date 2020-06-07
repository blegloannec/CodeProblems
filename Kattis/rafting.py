#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from math import hypot

def segment_point_dist(x1,y1, x2,y2, x,y):
    vx, vy = x2-x1, y2-y1         # seg. vec.
    nn = hypot(vx, vy)
    vx, vy = vx/nn, vy/nn         # normalized
    px, py = x-x1, y-y1
    dv = px*vx + py*vy            # projection on seg.
    if dv<0:
        return hypot(px, py)
    elif dv>nn:
        return hypot(x-x2, y-y2)
    nx, ny = -vy, vx              # normal vec.
    return abs(nx*px + ny*py)     # normal distance

def main():
    T = int(input())
    for _ in range(T):
        Ni = int(input())
        Pi = [tuple(map(int, input().split())) for _ in range(Ni)]
        No = int(input())
        Po = [tuple(map(int, input().split())) for _ in range(No)]
        dmin = float('inf')
        for x,y in Pi:
            for i in range(No):
                x1,y1 = Po[i-1]
                x2,y2 = Po[i]
                dmin = min(dmin, segment_point_dist(x1,y1, x2,y2, x,y))
        print(dmin/2.)

main()
