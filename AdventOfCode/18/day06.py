#!/usr/bin/env python3

import sys

from PIL import Image
import random
random.seed(42)

I = [tuple(map(int,L.strip().split(', '))) for L in sys.stdin.readlines()]
N = len(I)
X, Y = sorted(x for x,_ in I), sorted(y for _,y in I)
Xmin, Xmax = X[0], X[-1]
Ymin, Ymax = Y[0], Y[-1]

M = 15  # margin


# Part 1
def fill(x0,y0,x1,y1):
    Cnt = [0]*N
    Border = [False]*N
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            dmin = float('inf')
            D = []
            for i in range(N):
                a,b = I[i]
                d = abs(x-a)+abs(y-b)
                if d<dmin:
                    dmin = d
                    D = [i]
                elif d==dmin:
                    D.append(i)
            if len(D)==1:
                Cnt[D[0]] += 1
                if not (x0<x<x1 and y0<y<y1):
                    Border[D[0]] = True
    return Cnt,Border

C,B = fill(Xmin-M,Ymin-M,Xmax+M,Ymax+M)
print(max(C[i] for i in range(N) if not B[i]))


# Drawing the Manhattan distance Voronoi diagram (for fun)
def randcol():
    return tuple(random.randint(0,255) for _ in range(3))

def invcol(C):
    return tuple(255-c for c in C)

def draw_diagram(x0,y0,x1,y1):
    w,h = x1-x0+1,y1-y0+1
    Img = Image.new('RGB',(w,h))
    Pix = Img.load()
    Col = [randcol() for _ in range(N)]
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            dmin = float('inf')
            D = []
            for i in range(N):
                a,b = I[i]
                d = abs(x-a)+abs(y-b)
                if d<dmin:
                    dmin = d
                    D = [i]
                elif d==dmin:
                    D.append(i)
            if len(D)==1:
                Pix[x-x0,y-y0] = invcol(Col[D[0]]) if dmin==0 else Col[D[0]]
    Img.save('diagram6.png')
    Img.close()

#draw_diagram(Xmin-M,Ymin-M,Xmax+M,Ymax+M)


# Part 2
def dist(x0,y0,x1,y1,D):
    C = 0
    i,dx = 0,sum(abs(x0-x) for x in X)
    dy0 = sum(abs(y0-y) for y in Y)
    for x in range(x0,x1+1):
        j,dy = 0,dy0
        for y in range(y0,y1+1):
            # d can be naively computed in O(N):
            #   d = sum(abs(x-a)+abs(y-b) for a,b in I)
            # yet here we have it in O(1):
            d = dx+dy
            if d<D:
                C += 1
            # updating dy
            while j<N and y>=Y[j]:
                j += 1
            dy += j - (N-j)
        # updating dx
        while i<N and x>=X[i]:
            i += 1
        dx += i - (N-i)
    return C

print(dist(Xmin-M,Ymin-M,Xmax+M,Ymax+M,10000))
