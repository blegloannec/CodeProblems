#!/usr/bin/env python3

from fractions import gcd
from collections import deque

def lcm(a,b):
    return a*b//gcd(a,b)

W,H = map(int,input().split())
P,Q,R = map(int,input().split())
L = lcm(P-1,Q-1)
MW,MH = 2*W+1,2*H+1

def rand(x,y):
    return pow(R,pow(2,x+y*W+1,L),P*Q)&1

def gen_map():
    M = [['.' if 0<x<MW-1 and 0<y<MH-1 else '#' for x in range(MW)] for y in range(MH)]
    for y in range(H-1):
        for x in range(W-1):
            M[2*y+2][2*x+2] = '#'
            if rand(x,y):
                M[2*y+1][2*x+2] = '#'
            else:
                M[2*y+2][2*x+1] = '#'
    return M

M = gen_map()

def bfs(u0):
    D,P = {u0:0},{}
    Q = deque([u0])
    while Q:
        x,y = Q.popleft()
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=vx<MW and 0<=vy<MH and M[vy][vx]=='.' and (vx,vy) not in D:
                D[vx,vy] = D[x,y]+1
                P[vx,vy] = (x,y)
                Q.append((vx,vy))
    return D,P

def main():
    Dt,Pt = bfs((1,0))
    xt,yt = max((Dt[u],u) for u in Dt)[1]
    x,y = xt,yt
    path = []
    while (x,y) in Pt:
        path.append((x,y))
        x,y = Pt[x,y]
    Dx,_ = bfs((MW-2,MH-1))
    xx,yx = min((Dx[u],u) for u in path)[1]
    M[yx][xx] = 'X'
    M[yt][xt] = 'T'
    M[0][1] = '.'
    M[-1][-2] = '.'
    for L in M:
        print(''.join(L))

main()
