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
    bot.pop()
    bot += top[:0:-1]
    return bot

# recycled and improved from playingtheslots
# O(N) by a rotating-calipers-like technique
def rotating_edge_vertex_dist(P):
    N = len(P)
    dmin = float('inf')
    k = 1  # furthest vertex from current edge
    for i in range(N):
        xi,yi = P[i]
        j = (i+1)%N
        x0, y0 = P[j][0]-xi, P[j][1]-yi  # current edge
        n = dist(x0, y0)
        nx, ny = -y0/n, x0/n
        dk = abs((P[k][0]-xi)*nx + (P[k][1]-yi)*ny)
        l = (k+1)%N
        dl = abs((P[l][0]-xi)*nx + (P[l][1]-yi)*ny)
        while l!=i and dl>=dk:
            k, dk = l, dl
            l = (k+1)%N
            dl = abs((P[l][0]-xi)*nx + (P[l][1]-yi)*ny)
        dmin = min(dmin, dk)
    return dmin

def main():
    N,_ = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    P = [(float(x),float(y)) for x,y in andrew(P)]
    N = len(P)
    min_diam = 0. if N<=2 else rotating_edge_vertex_dist(P)
    print(min_diam)

main()
