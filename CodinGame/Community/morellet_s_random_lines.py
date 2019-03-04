#!/usr/bin/env python3

# The colors are well-defined because we add *complete* lines (not segments).
# Each time a *new* line is added, simply swap all the colors within
# one of the two half-planes it delimits.
# This does not create any issue as a line passes along an existing segment
# iff the whole line already exists.
# Given a line of equation ax+by+c=0, the sign of ax+by+c directly indicates
# the half-plane containing (x,y).

from fractions import gcd

Ax,Ay,Bx,By = map(int,input().split())
N = int(input())
P = set()
for _ in range(N):
    a,b,c = map(int,input().split())
    g = gcd(a,gcd(b,c))
    P.add((a//g,b//g,c//g))
sgn = lambda x: 0 if x==0 else 1 if x>0 else -1
S = 1
for a,b,c in P:
    S *= sgn(a*Ax+b*Ay+c) * sgn(a*Bx+b*By+c)
print(['NO','ON A LINE','YES'][S+1])
