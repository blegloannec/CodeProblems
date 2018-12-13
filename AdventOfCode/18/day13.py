#!/usr/bin/env python3

import sys, os
from PIL import Image

Dir = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}
Corner = {'/' : {(0,1):(-1,0),(-1,0):(0,1),(0,-1):(1,0),(1,0):(0,-1)},
          '\\': {(0,-1):(-1,0),(-1,0):(0,-1),(0,1):(1,0),(1,0):(0,1)}}

I = [list(L[:-1]) for L in sys.stdin.readlines()]
H,W = len(I),len(I[0])

# listing carts init. pos. and erasing them
Carts = []
for i in range(H):
    for j in range(W):
        if I[i][j] in Dir:
            di,dj = Dir[I[i][j]]
            Carts.append((i,j,di,dj,0))
            I[i][j] = '|' if di!=0 else '-'


# Simulation
def step(i,j,di,dj,t):
    i,j = i+di,j+dj
    c = I[i][j]
    if c in Corner:
        di,dj = Corner[c][di,dj]
    elif c=='+':
        if t==0:    # left
            di,dj = -dj,di
        elif t==2:  # right
            di,dj = dj,-di
        t = (t+1)%3
    return (i,j,di,dj,t)

def run(C0, stop_at_first_crash=False, gif_output=False):
    C = C0[:]
    t = 0
    while len(C)>1:
        Crash = [False]*len(C)
        for i in range(len(C)):
            if not Crash[i]:
                C[i] = step(*C[i])
                try:
                    j = next(j for j in range(len(C)) if j!=i and not Crash[j] and C[i][:2]==C[j][:2])
                    Crash[i] = Crash[j] = True
                    if stop_at_first_crash:
                        if gif_output:
                            gif_frame([C[i] for i in range(len(C)) if not Crash[i]],t,C[i][:2])
                        return C[i][:2]
                except:
                    pass
        C = sorted(C[i] for i in range(len(C)) if not Crash[i])
        if gif_output:
            gif_frame(C,t)
        t += 1
    return C[0][:2]


# GIF animation for the fun!
M = 1
A = 2*M+1
ColBack = (255,255,255)
ColPath = (192,192,192)
ColCart = (255,0,0)
ColCrash = (0,0,255)

def gif_empty_frame():
    Img = Image.new('RGB',(A*W,A*H),ColBack)
    Pix = Img.load()
    for i in range(H):
        for j in range(W):
            c = I[i][j]
            if c!=' ':
                Pix[A*j+M,A*i+M] = ColPath
                if c=='-' or c=='+':
                    for dj in range(-M,A+M):
                        Pix[A*j+dj,A*i+M] = ColPath
                if c=='|' or c=='+':
                    for di in range(-M,A+M):
                        Pix[A*j+M,A*i+di] = ColPath
    return Img

Img0 = gif_empty_frame()

def gif_frame(C, t, crash=None):
    assert(0<=t<1000)
    Img = Img0.copy()
    Pix = Img.load()
    for i,j,di,dj,_ in C:
        Pix[A*j+M,A*i+M] = ColCart
        Pix[A*j+M+dj,A*i+M+di] = ColCart
        Pix[A*j+M-di,A*i+M+dj] = ColCart
        Pix[A*j+M+di,A*i+M-dj] = ColCart
    if crash is not None:
        i,j = crash
        for di in range(-1,2):
            for dj in range(-1,2):
                Pix[A*j+M+dj,A*i+M+di] = ColCrash
        Img.save('gif13/last_frame.gif')
    else:
        Img.save('gif13/frame%03d.gif' % t)
    Img.close()


# Part 1
gif_output = False
x,y = run(Carts,True,gif_output)
if gif_output:
    os.system('convert -loop 0 -delay 4 gif13/frame*.gif -delay 150 gif13/last_frame.gif anim13.gif')
print('%d,%d' % (y,x))

# Part 2
x,y = run(Carts)
print('%d,%d' % (y,x))
