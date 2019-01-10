#!/usr/bin/env python3

import sys, re
from heapq import *
from itertools import product

class Point:
    def __init__(self, x=0,y=0,z=0):
        self.x,self.y,self.z = x,y,z

def dist(X,Y):
    return abs(X.x-Y.x)+abs(X.y-Y.y)+abs(X.z-Y.z)

form = re.compile('pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')
I = [tuple(map(int,form.match(L.strip()).groups())) for L in sys.stdin.readlines()]
N = len(I)
P = [Point(x,y,z) for x,y,z,_ in I]
R = [r for _,_,_,r in I]


# Part 1
imax = max(range(N), key=(lambda i: R[i]))
cpt = 0
for j in range(N):
    if dist(P[imax],P[j])<=R[imax]:
        cpt += 1
print(cpt)


# Part 2 - Octree scan
# NB: My first idea was to compute the pairwise intersection graph of the balls and
#     to compute its max clique by randomly generating a maximal (for inclusion)
#     independent sets of the complementary.
#     This works very well (the 989 max clique is found in more than 9 random
#     generations of out of 10, without any heuristic in the generation).
#     However this is only a necessary condition for a global intersection, and,
#     unfortunately, the minimum radius of a ball centered in 0 to join this clique
#     is the solution-1! This gives a very good lower bound, yet I can't think of any way
#     to reinforce the condition without actually leading to a better solution, so...
Zero = Point(0,0,0)
Inf = float('inf')

class Box:
    def __init__(self, x0,y0,z0, x1,y1,z1):
        self.x0,self.y0,self.z0 = x0,y0,z0
        self.x1,self.y1,self.z1 = x1,y1,z1
        
    def __lt__(self, _):  # to be usable in heaps
        return False      # simply => component skipped in the tuple

    def is_singleton(self):
        return self.x0==self.x1 and self.y0==self.y1 and self.z0==self.z1

    def subboxes(self):
        if self.x0<self.x1:
            xm = (self.x0+self.x1)//2
            X = [(self.x0,xm),(xm+1,self.x1)]
        else:
            X = [(self.x0,self.x0)]
        if self.y0<self.y1:
            ym = (self.y0+self.y1)//2
            Y = [(self.y0,ym),(ym+1,self.y1)]
        else:
            Y = [(self.y0,self.y0)]
        if self.z0<self.z1:
            zm = (self.z0+self.z1)//2
            Z = [(self.z0,zm),(zm+1,self.z1)]
        else:
            Z = [(self.z0,self.z0)]
        for (xa,xb),(ya,yb),(za,zb) in product(X,Y,Z):
            yield Box(xa,ya,za,xb,yb,zb)

def box_point_dist(B,X):
    d = 0
    if not B.x0<=X.x<=B.x1:
        d += B.x0-X.x if X.x<B.x0 else X.x-B.x1
    if not B.y0<=X.y<=B.y1:
        d += B.y0-X.y if X.y<B.y0 else X.y-B.y1
    if not B.z0<=X.z<=B.z1:
        d += B.z0-X.z if X.z<B.z0 else X.z-B.z1
    return d

def octree(B0,J0):
    # /!\ lower/upper bounds are sign inversed because of *min* heaps in Python
    lower_bound = (Inf,-Inf)  # best solution so far (/!\ inversed)
    d0 = (-len(J0),box_point_dist(B0,Zero))
    Boxes = [(d0,B0,J0)]
    while Boxes:
        d,B,J = heappop(Boxes)
        if d>=lower_bound:
            break
        if B.is_singleton():
            lower_bound = d
            continue
        for SB in B.subboxes():
            # balls intersecting the box
            SJ = tuple(j for j in J if box_point_dist(SB,P[j])<=R[j])
            # best possible solution in the box (/!\ inversed)
            box_upper_bound = (-len(SJ),box_point_dist(SB,Zero))
            if box_upper_bound<lower_bound:
                heappush(Boxes,(box_upper_bound,SB,SJ))
    return lower_bound[1]

x0,x1 = min(X.x-r for X,r in zip(P,R)),max(X.x+r for X,r in zip(P,R))
y0,y1 = min(X.y-r for X,r in zip(P,R)),max(X.y+r for X,r in zip(P,R))
z0,z1 = min(X.z-r for X,r in zip(P,R)),max(X.z+r for X,r in zip(P,R))
B0 = Box(x0,y0,z0,x1,y1,z1)
J0 = tuple(range(N))
print(octree(B0,J0))
