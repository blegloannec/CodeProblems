#!/usr/bin/env python

from math import sqrt

# runs in 9s with pypy

N = 2500000

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = P[1] = False
    for i in xrange(2,N):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

# sieving to get enough primes
P = sieve(40*N)

# computing points
def points(n):
    XY = [(2,2)]
    x,y,i = 2,2,3
    even = False
    while len(XY)<N:
        if P[i]:
            x += i
            y += i if even else -i
            if even:
                XY.append((x,y))
            even = not even
        i += 2
    return XY

def left_turn(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1])-(a[1]-c[1])*(b[0]-c[0])>0

def main():
    pts = points(N)
    S = 0
    top = [0]
    for i in xrange(1,N):
        # updating the (upper) convex hull (Andrew's algo)
        while len(top)>=2 and not left_turn(pts[i],pts[top[-1]],pts[top[-2]]):
            top.pop()
        top.append(i)
        # counting points that are visible from the last peak
        # we stop at the previous point of the convex hull
        # (we only explore the last convex section of the curve)
        # because we cannot see any further (and we hope that point
        # is not far, which is the case)
        # algo would be O(N^2) if the curve was convex
        # fortunately it is almost concave so we are close to O(N)
        dx0,dy0 = 0,1
        for j in xrange(i-1,top[-2]-1,-1):
            dx,dy = pts[i][0]-pts[j][0],pts[i][1]-pts[j][1]
            if dy*dx0<dy0*dx:
                dx0,dy0 = dx,dy
                S += 1
    print S

main()
