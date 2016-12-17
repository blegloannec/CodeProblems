#!/usr/bin/env python

import hashlib
from collections import deque

Input = 'hhhxzeay'

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

V = ['U','D','L','R']
DX = [0,0,-1,1]
DY = [-1,1,0,0]

def bfs():
    MinP,MaxL = None,0
    Q = deque([(0,0,'')])
    while Q:
        x,y,p = Q.popleft()
        if x==3 and y==3:
            if MinP==None: # Part One
                MinP = p
            MaxL = len(p) # Part Two
            continue
        O = md5(Input+p)
        for i in xrange(4):
            if ord('b')<=ord(O[i])<=ord('f'):
                vx,vy = x+DX[i],y+DY[i]
                if 0<=vx<=3 and 0<=vy<=3:
                    Q.append((vx,vy,p+V[i]))
    return MinP,MaxL

print bfs()
