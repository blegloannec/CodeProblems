#!/usr/bin/env python3

import sys, re, os
from PIL import Image

form = re.compile('position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>')
I = [tuple(map(int,form.match(L.strip()).groups())) for L in sys.stdin.readlines()]

# Part 1 & 2
def pic(t, out=False):
    X = [px+t*vx for px,_,vx,_ in I]
    Y = [py+t*vy for _,py,_,vy in I]
    x0,y0 = min(X),min(Y)
    W,H = max(X)-x0+1,max(Y)-y0+1
    if out:
        assert(max(W,H)<=100)
        O = [[' ']*W for _ in range(H)]
        for x,y in zip(X,Y):
            O[y-y0][x-x0] = '#'
        print('\n'.join(''.join(L) for L in O))
    return (W,H)

tmin = min(range(15000),key=pic)
pic(tmin,True)
print(tmin)


# GIF anim for the fun!
def gif_frames(t0,t1):
    X,Y = [],[]
    x0 = y0 = float('inf')
    x1 = y1 = float('-inf')
    for t in range(t0,t1+1):
        X.append([px+t*vx for px,_,vx,_ in I])
        Y.append([py+t*vy for _,py,_,vy in I])
        x0,y0 = min(x0,min(X[-1])),min(y0,min(Y[-1]))
        x1,y1 = max(x1,max(X[-1])),max(y1,max(Y[-1]))
    W,H = x1-x0+1,y1-y0+1
    assert(max(W,H)<=500)
    for t in range(len(X)):
        Img = Image.new('1',(W,H))
        Pix = Img.load()
        for x,y in zip(X[t],Y[t]):
            Pix[x-x0,y-y0] = 1
        if t==len(X)-1:
            Img.save('gif10/last_frame.gif')
        else:
            Img.save('gif10/frame%03d.gif' % t)
        Img.close()

#gif_frames(tmin-30,tmin)
# using ImageMagick to animate:
#os.system('convert -delay 6 -loop 0 gif10/frame*.gif -delay 90 gif10/last_frame.gif anim10.gif')
