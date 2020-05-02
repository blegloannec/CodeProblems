#!/usr/bin/env python3

import sys

# Recycled from CG/morellet_s_random_lines.py
# The colors are well-defined because we add *complete* lines (not segments).
# Each time a *new* line is added, simply swap all the colors within
# one of the two half-planes it delimits.
# Given a line of equation ax+by+c=0, the sign of ax+by+c directly indicates
# the half-plane containing (x,y).

sgn = lambda x: 0 if x==0 else 1 if x>0 else -1

def main():
    S = int(sys.stdin.readline())
    L = []
    for _ in range(S):
        x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
        dx = x1-x2
        dy = y1-y2
        a,b = -dy,dx
        c = -(a*x1+b*y1)
        #assert a*x2+b*y2+c==0
        L.append((a,b,c))
    T = int(sys.stdin.readline())
    for _ in range(T):
        x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
        S = 1
        for a,b,c in L:
            S *= sgn(a*x1+b*y1+c) * sgn(a*x2+b*y2+c)
        sys.stdout.write('different\n' if S<0 else 'same\n')

main()
