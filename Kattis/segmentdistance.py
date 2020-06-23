#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from math import hypot

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __sub__(self, A):
        return Point(self.x-A.x, self.y-A.y)
    def __mul__(self, A):     # * for cross product
        return self.x*A.y - self.y*A.x 
    def __matmul__(self, A):  # @ for dot product
        return self.x*A.x + self.y*A.y
    def __abs__(self):        # abs for norm
        return hypot(self.x, self.y)
    def __eq__(self, A):
        return self.x==A.x and self.y==A.y

# adapted from Kattis/rafting.py
def segment_point_dist(A,B, P):
    if A==B:                   # segment is a point
        return abs(P-A)
    V = B-A                    # seg. vec.
    nn = abs(V)
    V = Point(V.x/nn, V.y/nn)  # normalized
    Q = P-A
    dv = Q@V                   # projection on seg.
    if dv<0:
        return abs(Q)
    elif dv>nn:
        return abs(P-B)
    N = Point(-V.y, V.x)       # normal vec.
    return abs(Q@N)            # normal distance

def sign(x):
    if x==0:
        return 0
    return 1 if x>0 else -1

# adapted from Kattis/countingtriangles.cpp
def segment_intersect(A1,B1, A2,B2):
    if A1==A2 or A1==B2 or B1==A2 or B1==B2:
        return True
    V1 = B1-A1
    V2 = B2-A2
    #if V1*V2==0:  # // or aligned
    #    return False
    # general case: testing sides
    return sign(V1*(A2-A1))!=sign(V1*(B2-A1)) and  \
        sign(V2*(A1-A2))!=sign(V2*(B1-A2))

def main():
    N = int(input())
    for _ in range(N):
        x1,y1, x2,y2, x3,y3, x4,y4 = map(int, input().split())
        A1, B1, A2, B2 = Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4)
        if segment_intersect(A1,B1, A2,B2):
            d = 0
        else:
            d = min(segment_point_dist(A1,B1, A2),
                    segment_point_dist(A1,B1, B2),
                    segment_point_dist(A2,B2, A1),
                    segment_point_dist(A2,B2, B1))
        sys.stdout.write(f'{d:.2f}\n')

main()
