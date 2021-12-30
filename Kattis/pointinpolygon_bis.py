#!/usr/bin/env python3

from math import atan2, pi

def inside_non_convex(Polygon, P):
    if P in Polygon:
        return 'on'
    EPS = 1e-9
    wa = 0.  # winding angle
    x,y = P
    A = [atan2(y1-y,x1-x) for x1,y1 in Polygon]
    for i in range(len(A)):
        da = A[(i+1)%len(A)] - A[i]
        if abs(abs(da)-pi)<EPS:  # half-turn <=> on an edge
            return 'on'
        if   da> pi: da -= 2*pi
        elif da<-pi: da += 2*pi
        wa += da
    wn = round(wa/pi)
    return 'out' if wn==0 else 'in'

def main():
    while True:
        N = int(input())
        if N<=0:
            break
        Polygon = [tuple(map(int,input().split())) for _ in range(N)]
        M = int(input())
        for _ in range(M):
            P = tuple(map(int,input().split()))
            print(inside_non_convex(Polygon,P))

main()
