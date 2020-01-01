#!/usr/bin/env python3

import os
from PIL import Image
from collections import deque

I = [[-9, -1, -1], [2, 9, 5], [10, 18, -12], [-6, 15, -7]]  # Input

sgn = lambda x: 0 if x==0 else 1 if x>0 else -1

def simu_anim(I, T):
    N,D = len(I),len(I[0])
    X = [L[:] for L in I]
    V = [[0]*D for _ in range(N)]
    dimx,dimy = 0,1
    Col = ((255,0,0),(255,255,0),(0,255,255),(255,0,255),(0,0,0))
    S = 190
    L = 12
    Img = Image.new('RGB', (2*S,2*S), Col[-1])
    Pix = Img.load()
    Q = [deque() for _ in range(N)]
    for t in range(T):
        for i in range(N):
            for j in range(i+1,N):
                for k in range(D):
                    dv = sgn(X[i][k]-X[j][k])
                    V[i][k] -= dv
                    V[j][k] += dv
        for i in range(N):
            if len(Q[i])>L:
                Pix[Q[i].popleft()] = Col[-1]
            for k in range(D):
                X[i][k] += V[i][k]
            Q[i].append((X[i][dimx]+S,X[i][dimy]+S))
            Pix[Q[i][-1]] = Col[i]
        Img.save('anim12/frame%04d.gif' % t)

os.system('mkdir anim12')
simu_anim(I,1000)
os.system('gifsicle -O3 -l -d3 anim12/frame*.gif > anim12.gif')
os.system('rm -rf anim12')
