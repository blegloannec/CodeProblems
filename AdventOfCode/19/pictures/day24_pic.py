#!/usr/bin/env python3

import sys, os, random
from PIL import Image
random.seed(42)

S = 100
S2 = S*S
A = [int(random.random()>0.98) for _ in range(S2)]

def step(A):
    B = [0]*S2
    for x in range(S):
        for y in range(S):
            s = 0
            for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                #if 0<=vx<S and 0<=vy<S:
                vx %= S  # torus
                vy %= S
                s += A[S*vy+vx]
            B[S*y+x] = int(s==1 if A[S*y+x] else 1<=s<=2)
    return B

def pic(A):
    Img = Image.new('1',(S,S))
    Img.putdata([1-a for a in A])
    return Img

os.system('mkdir anim24')
for t in range(900):
    if t&1==0:
        Img = pic(A).resize((4*S,4*S))
        Img.save('anim24/frame%04d.gif' % t)
        Img.close()
    A = step(A)
os.system('gifsicle -O3 -l -d4 anim24/frame*.gif > anim24.gif')
os.system('rm -r anim24')
