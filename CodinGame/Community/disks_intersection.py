#!/usr/bin/env python3

from math import *

def circles_intersection_area(C1, C2):
    (x1,y1,r1), (x2,y2,r2) = C1, C2
    # distance^2 between centers
    d2 = (x1-x2)**2 + (y1-y2)**2
    if d2>=(r1+r2)**2:
        # no intersection
        return 0.
    if d2<=(r1-r2)**2:
        # one circle inside the other
        return pi*min(r1,r2)**2
    # d distance between centers
    # without loss of generality, we consider
    # the circles centered in (0,0) and (d,0)
    d = sqrt(d2)
    # intersection points (x, +/-y)
    x = (r1**2 - r2**2 + d2) / (2.*d)
    y = sqrt(r1**2 - x**2)
    # circle sectors areas
    a1 = r1**2 * atan2(y,x)
    a2 = r2**2 * atan2(y,d-x)
    # intersection area =
    #    sum of sectors
    #  - centers+intersections quadrilateral area
    A = a1+a2 - d*y
    return A

if __name__=='__main__':
    C1 = tuple(map(float,input().split()))
    C2 = tuple(map(float,input().split()))
    A = circles_intersection_area(C1,C2)
    print('{:.2f}'.format(round(A,2)))
