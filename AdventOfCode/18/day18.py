#!/usr/bin/env python3

import sys, os
from collections import Counter
from PIL import Image

I = [list(L.strip()) for L in sys.stdin.readlines()]
H,W = len(I),len(I[0])


# GIF anim for the fun!
def gif_frame(C,t):
    Col = {'.':(152,118,84),'|':(1,68,33),'#':(101,67,33)}
    Img = Image.new('RGB',(W,H))
    Pix = Img.load()
    for i in range(H):
        for j in range(W):
            Pix[j,i] = Col[C[i][j]]
    Img.resize((4*W,4*H)).save('gif18/frame%03d.gif' % t)
    Img.close()


# Part 1 & 2
def step(C):
    D = [L[:] for L in C]
    for i in range(H):
        for j in range(W):
            V = Counter(C[x][y] for x in range(i-1,i+2) if 0<=x<H for y in range(j-1,j+2) if 0<=y<W and (x,y)!=(i,j))
            if C[i][j]=='.' and V['|']>=3:
                D[i][j] = '|'
            elif C[i][j]=='|' and V['#']>=3:
                D[i][j] = '#'
            elif C[i][j]=='#' and not (V['#']>=1 and V['|']>=1):
                D[i][j] = '.'
    return D

def run(C, T, anim=False):
    Time = {}
    for t in range(T):
        #print('\n'.join(''.join(L) for L in C))
        if anim:
            gif_frame(C,t)
        K = tuple(tuple(L) for L in C)  # hashable
        if K in Time:
            break
        Time[K] = t
        C = step(C)
    if t<T-1:                           # ultimately periodic
        t0,p = Time[K],t-Time[K]        # loop start, period
        T = (T-t0)%p + t0
        C = next(C for C in Time if Time[C]==T)
    return sum(L.count('|') for L in C) * sum(L.count('#') for L in C)

print(run(I,10))


# Part 2
gif_anim = False
print(run(I,10**9,gif_anim))
if gif_anim:
    os.system('convert -loop 0 -delay 2 gif18/frame*.gif anim18.gif')
