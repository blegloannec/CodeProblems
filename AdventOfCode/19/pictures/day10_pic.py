#!/usr/bin/env python3

import sys, os
from math import atan2, pi
from PIL import Image, ImageDraw
from itertools import groupby
from collections import deque

I = [L.strip() for L in sys.stdin.readlines()]
H,W = len(I),len(I[0])
A = [(j,i) for i in range(H) for j in range(W) if I[i][j]=='#']

PREC = 9
def angle(x,y):
    a = -atan2(-y,x)  # /!\ clockwise & inverse y
    if a<0:
        a += 2.*pi
    a -= 3.*pi/2.     # 0 is up
    if a<0:
        a += 2.*pi
    return round(a,PREC)

dist2 = lambda x,y: x*x+y*y


# Part 1
smax = 0
for x,y in A:
    s = len(set(angle(ya-y,xa-x) for xa,ya in A if (xa,ya)!=(x,y)))
    if s>smax:
        smax = s
        x0,y0 = x,y


# Part 2
X0 = sorted((angle(xa-x0,ya-y0), dist2(xa-x0,ya-y0), (xa,ya)) for xa,ya in A if (xa,ya)!=(x0,y0))
X = deque(deque(p for _,_,p in L) for _,L in groupby(X0, (lambda x: x[0])))
os.system('mkdir anim10')
a = 4
Img = Image.new('RGB', (a*W,a*H), (0,0,0))
Pix = Img.load()
for x,y in A:
    Pix[a*x,a*y] = (220,220,220)
t = 0
while X:
    L = X.popleft()
    x,y = L.popleft()
    Img0 = Img.copy()
    Drw = ImageDraw.Draw(Img0)
    Drw.line((a*x0,a*y0,a*x,a*y), fill=(255,100,100))
    Pix0 = Img0.load()
    Pix0[a*x0,a*y0] = (0,0,255)
    Pix0[a*x,a*y] = (255,0,0)
    Img0.resize((2*a*W,2*a*H)).save('anim10/frame%04d.gif' % t)
    Img0.close()
    t += 1
    Pix[a*x,a*y] = (0,0,0)
    if L:
        X.append(L)
Img.close()
#os.system('convert -loop 0 -delay 5 anim10/*.gif anim10.gif')
os.system('gifsicle -O3 -d5 -l anim10/*.gif > anim10.gif')
os.system('rm -r anim10')
