#!/usr/bin/env python3

import sys
from math import sqrt
from collections import defaultdict

def parse_particle(L):
    L = L.strip().split(', ')
    return tuple(tuple(map(int,L[i][3:-1].split(','))) for i in range(3))

P = list(map(parse_particle,sys.stdin.readlines()))


# Part 1
def norm(X):
    return sum(abs(x) for x in X)

V = [(norm(P[i][2]),i) for i in range(len(P))]
print(min(V)[1])  # as there is a unique minimum acceleration particle here


# Part 2 - O(n^2) collisions computation and time sweeping (in O(n^2 log(n)) in the worst case)
# (NB: according to the subreddit, a naive simulation was good enough here...)
# v(t) = v0 + t*a
# p(t) = p(t-1) + v(t)
#      = p0 + v(1) + ... + v(t)
#      = p0 + (v0+a) + (v0+2a) + ... + (v0+ta)
#      = p0 + v0*t + a*t(t+1)/2
#      = a/2 * t^2 + (v0+a/2) * t + p0

def roots(a,b,c):  # positive integer roots of ax^2 + bx + c = 0
    if a==0:
        if b==0:
            return set() if c!=0 else None  # None is our code for 0 = 0 (everything is solution)
        if b!=0 and c%b==0 and -c//b>0:
            return {-c//b}
        return set()
    D = b*b-4*a*c
    if D<0:
        return set()
    d = int(sqrt(D))
    R = set()
    if d*d==D:
        for e in [-d,d]:
            if (-b+e)%(2*a)==0:
                r = (-b+e)//(2*a)
                if r>0:
                    R.add(r)
    return R

def collision(i,j):
    R = None
    for d in range(3):
        a0,b0,c0 = P[i][2][d],2*P[i][1][d]+P[i][2][d],2*P[i][0][d]
        a1,b1,c1 = P[j][2][d],2*P[j][1][d]+P[j][2][d],2*P[j][0][d]
        r = roots(a0-a1,b0-b1,c0-c1)
        if R==None:
            R = r
        elif r!=None:
            R &= r
    return min(R) if R else None

C = {}     # collisions
E = set()  # eliminated particles
# computing collisions
for i in range(len(P)):
    for j in range(i+1,len(P)):
        assert(P[i][0]!=P[j][0])  # just to make sure there is no t=0 collision
        # collision time
        t = collision(i,j)
        if t:
            if t not in C:
                C[t] = defaultdict(set)
            # collision point
            p = tuple(P[i][0][d]+P[i][1][d]*t+P[i][2][d]*t*(t+1)//2 for d in range(3))
            C[t][p].add(i)
            C[t][p].add(j)
# time sweeping
for t in sorted(C.keys()):
    for p in C[t]:  # for each collision point at that time
        C[t][p] -= E
        if len(C[t][p])>=2:
            E |= C[t][p]
print(len(P)-len(E))
