#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2000)
from math import pi, cos, sin

def dfs_width(u=0, u0=-1):
    V = [v for v in T[u] if v!=u0]
    wv = 0
    for v in T[u]:
        if v!=u0:
            dfs_width(v,u)
            wv += W[v]
    W[u] = max(1,len(V),wv)

def dfs_plot(u=0, u0=-1, x=0., y=0., a=0., b=2.*pi):
    P[u] = (x,y)
    V = [v for v in T[u] if v!=u0]
    if V:
        w = sum(W[v] for v in V)
        w0 = 0
        for v in V:
            av = a + (b-a)*w0/w
            w0 += W[v]
            bv = a + (b-a)*w0/w
            dfs_plot(v, u, x+cos((av+bv)/2.), y+sin((av+bv)/2.), av, bv)

def make_svg():
    S = 10.
    A = 30.
    O = ['<svg width="{}" height="{}">'.format(A*2*S,A*2*S)]
    O.append('<g transform="scale({} {})">'.format(A,A))
    for u in range(N):
        x1,y1 = P[u]
        for v in T[u]:
            if u<v:
                x2,y2 = P[v]
                O.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="blue" stroke-width="0.01" />'.format(x1+S,y1+S,x2+S,y2+S))
    O.append('</g>')
    O.append('</svg>')
    F = open('out.svg', 'w')
    F.write('\n'.join(O))
    F.close()

def main():
    global N,T,P,W
    N = int(input())
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        T[u].append(v)
        T[v].append(u)
    W = [None]*N
    dfs_width()
    P = [None]*N
    dfs_plot()
    for p in P:
        print(*p)
    #make_svg()

main()
