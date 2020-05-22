#!/usr/bin/env python3

# see also playingtheslots.py for a simpler variant

import sys
from math import sqrt
input = sys.stdin.readline

dist = lambda x,y: sqrt(x*x + y*y)

def left_turn(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0

def andrew(S):
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top)>=2 and not left_turn(p,top[-1],top[-2]):
            top.pop()
        top.append(p)
        while len(bot)>=2 and not left_turn(bot[-2],bot[-1],p):
            bot.pop()
        bot.append(p)
    return bot[:-1]+top[:0:-1]

# recycled and improved from playingtheslots
def ternary_search(P, i):
    N = len(P)
    j = (i+1)%N
    xi,yi = P[i]
    x0, y0 = P[j][0]-xi, P[j][1]-yi
    n = dist(x0, y0)
    nx, ny = -y0/n, x0/n
    l, r = i+2, i+N-1
    while l%N!=r%N:
        m1 = (l+r)//2
        k = m1%N
        d1 = abs((P[k][0]-xi)*nx + (P[k][1]-yi)*ny)
        m2 = m1+1
        k = m2%N
        d2 = abs((P[k][0]-xi)*nx + (P[k][1]-yi)*ny)
        if d1==d2:
            l = r = m1
        elif d1<d2:
            l = m2
        else:
            r = m1
    k = l%N
    return abs((P[k][0]-xi)*nx + (P[k][1]-yi)*ny)

def main():
    N,_ = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    P = [(float(x),float(y)) for x,y in andrew(P)]
    N = len(P)
    min_diam = 0. if N<=2 else min(ternary_search(P,i) for i in range(N))
    print(min_diam)

main()
