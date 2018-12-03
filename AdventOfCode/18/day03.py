#!/usr/bin/env python3

import sys, re
from collections import defaultdict

form = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
I = [tuple(map(int,form.match(L).groups())) for L in sys.stdin.readlines()]

# Part 1
## Method 1 (probably expected): naive marking of rectangles
##     O(n*s^2) for s the size of the space (~1000 here)
## NB: can be done in O(n^3) splitting the x/y-axis by the 2n x/y-bound
##     of the rectangles, thus reducing the space to ~ 4n^2
D = defaultdict(int)
for _,x,y,w,h in I:
    for i in range(x,x+w):
        for j in range(y,y+h):
            D[i,j] += 1
print(sum(int(D[p]>1) for p in D))

## Method 2: sweep line in O(n^2)
def rectangle_union(I):
    X = []
    Y = []
    for i in range(len(I)):
        _,x,y,w,h = I[i]
        X.append(x)
        X.append(x+w)
        Y.append((y,i))
        Y.append((y+h,i))
    X.sort()
    X = [X[i] for i in range(len(X)) if i==0 or X[i]!=X[i-1]]  # uniq
    NumX = {X[i]:i for i in range(len(X))}  # rev
    Y.sort()
    C = [0]*(len(X)-1)
    j = Area = yprev = 0
    while j<len(Y):
        y0 = Y[j][0]
        # /!\ in the next line, the test is C[k]>1 as we want to count the
        #     area covered by *at least 2* rectangles
        #     for the *usual union*, change it to C[k]>0
        Area += sum((X[k+1]-X[k])*(y0-yprev) for k in range(len(C)) if C[k]>1)
        while j<len(Y) and Y[j][0]==y0:
            _,x,y,w,_ = I[Y[j][1]]
            d = 1 if y0==y else -1
            for k in range(NumX[x],NumX[x+w]):
                C[k] += d
            j += 1
        yprev = y0
    return Area

#print(rectangle_union(I))


# Part 2
## Method 1: easy second pass after part 1
for ID,x,y,w,h in I:
    if all(D[i,j]==1 for i in range(x,x+w) for j in range(y,y+h)):
        print(ID)

## Method 2: O(n^2) through rectangle intersections (independent from part 1)
def intersect(i,j):
    _,xi,yi,wi,hi = I[i]
    _,xj,yj,wj,hj = I[j]
    return max(xi,xj)<min(xi+wi,xj+wj) and max(yi,yj)<min(yi+hi,yj+hj)

def method2():
    for i in range(len(I)):
        if not any(intersect(i,j) for j in range(len(I)) if i!=j):
            print(I[i][0])

#method2()
