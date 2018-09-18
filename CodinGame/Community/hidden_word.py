#!/usr/bin/env python3

def mark(x0,y0,dx,dy):
    while 0<=x0<h and 0<=y0<w:
        x,y = x0,y0
        u = ''
        while 0<=x<h and 0<=y<w:
            u += G[x][y]
            if u in W or u[::-1] in W:
                i,j = x,y
                for _ in range(len(u)):
                    M[i][j] = False
                    i,j = i-dx,j-dy
            x,y = x+dx,y+dy
        x0,y0 = x0+dx,y0+dy

def main():
    global W,h,w,G,M
    n = int(input())
    W = set(input() for _ in range(n))
    h,w = map(int,input().split())
    G = [input() for _ in range(h)]
    M = [[True]*w for _ in range(h)]
    for i in range(h):
        mark(i,0,0,1)
        mark(i,0,1,1)
        mark(i,0,-1,1)
    for j in range(w):
        mark(0,j,1,0)
        if j>0:
            mark(0,j,1,1)
            mark(h-1,j,-1,1)
    res = []
    for i in range(h):
        for j in range(w):
            if M[i][j]:
                res.append(G[i][j])
    res = ''.join(res)
    print(res)

main()
