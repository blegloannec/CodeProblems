#!/usr/bin/env python3

from math import atan2

# That's actually a nice geometry problem: Given a list of 2D vectors,
# find the largest euclidean norm of a subset-sum vector.

# Method 0 (not implemented): O(N^2 log N) DP + convex hull
# NB: This is also the editorial intended approach.
# Maintaining the set of possible sums adding the points one by one
# would obviously lead to an exponential explosion. However the only
# "valuable" points are the "furthest" in all directions, i.e. those
# that belong to the convex hull.
# Hence, we maintain a convex polygon of the valuable sums.
# Each time we consider a new vector V, computing the new sums is
# geometrically equivalent to duplicate the polygon and translate one
# copy by V. Computing the new convex hull of the updated sums is
# geometrically equivalent to cut the previous polygon in half,
# translate one half by V, and link both parts, which should create
# at most 4 new points, thus avoiding the exponential explosion.


# Method 1: O(N^2) good enough approach
# Let us imagine we know the optimal vector/direction D, how would we
# pick the vectors to build it? Simply pick those that have a positive
# dot product with D (in other words, those that are in the half-plane
# defined by V as an orthogonal vector).
# Consequently, sort the vectors by angle around O, the solution has to
# be a contiguous subarray, seeing the sorted array as circular, with
# a maximum angular difference of pi (otherwise it is sub-optimal).
# The following code enumerates every subarray in O(N^2), without even
# caring about the angle constraint.
def max_vec_sum_ON2(X,Y):
    P = [(x,y) for x,y in zip(X,Y) if not x==y==0]
    N = len(P)
    P.sort(key=(lambda p: atan2(p[1],p[0])))
    res = 0
    for i in range(N):
        sx,sy = P[i]
        j = (i+1)%N
        res = max(res, sx*sx+sy*sy)
        while j!=i:
            sx += P[j][0]
            sy += P[j][1]
            res = max(res, sx*sx+sy*sy)
            j = (j+1)%N
    return res


# Method 2: O(N log N) optimal approach
# Same as method 1 except we use a two-pointer technique to
# enumerate in O(N) the "maximal pi-angled" (/ half-plane)
# windows leaning on each point.
# This is trickier as we have to consider several cases each time:
#  - Include or exclude the point the window leans on;
#  - Consider both the window and its complementary (to avoid
#    having to do a second pass in the other direction).
def cross(p,q):
    return p[0]*q[1] - p[1]*q[0]

def max_vec_sum(X,Y):
    P = [(x,y) for x,y in zip(X,Y) if not x==y==0]
    N = len(P)
    P.sort(key=(lambda p: atan2(p[1],p[0])))
    SX,SY = sum(X),sum(Y)
    sx = sy = res = j = 0
    for i in range(N):
        if j==i:
            sx += P[i][0]
            sy += P[i][1]
            j = (i+1)%N
        while j!=i and cross(P[i],P[j])>=0:
            sx += P[j][0]
            sy += P[j][1]
            res = max(res, sx**2+sy**2, (SX-sx)**2+(SY-sy)**2)
            j = (j+1)%N
        sx -= P[i][0]
        sy -= P[i][1]
        res = max(res, sx**2+sy**2, (SX-sx)**2+(SY-sy)**2)
    return res


# MAIN
if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        print(max_vec_sum(A,B))
