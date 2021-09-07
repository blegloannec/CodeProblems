#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image

src = Image.open('mandelbrot.gif','r')
# image avec palette

w,h = 640,480
img = Image.new('P',(w,h))
img.palette = src.palette # on prend la même palette
pix = img.load()
xmin,dx,ymin,dy = 0.34,0.036,0.57,0.027
#xmin,dx,ymin,dy = -2.0,3.0,-1.0,2.0
imax = 128
for x in range(w):
    for y in range(h):
        rx = xmin+x*dx/w
        ry = ymin+(h-1-y)*dy/h
        i = 0
        a,b = 0.0,0.0
        while i<imax and a**2+b**2<=4:
            sa = a
            a = a**2-b**2+rx
            b = 2*sa*b+ry
            i += 1
        pix[x,y] = i-1
img.save('mandelout.gif')

# On compare les images, il y a 1679 différences
data = filter(lambda (x,y):x!=y, zip(src.tostring(),img.tostring()))
print len(data)

# 1979 = 23 x 73
# On refait le coup du niveau 30 !
diff = map(lambda (x,y):ord(x)-ord(y), data)
dst = Image.new('1',(23,73))
dst.putdata(map(lambda x:0 if x<0 else 1, diff))
dst.save('arecibo.gif')
