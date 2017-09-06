#!/usr/bin/env python3

# NB: "On the given test cases, the ant never has to go out of bounds."

Dir = {'N':(-1,0),'E':(0,1),'S':(1,0),'W':(0,-1)}
Swap = {'.':'#','#':'.'}

W,H = map(int,input().split())
y,x = map(int,input().split())
dx,dy = Dir[input()]
T = int(input())
G = [list(input()) for _ in range(H)]
for _ in range(T):
    dx,dy = (dy,-dx) if G[x][y]=='#' else (-dy,dx)
    G[x][y] = Swap[G[x][y]]
    x,y = x+dx,y+dy
for L in G:
    print(''.join(L))
