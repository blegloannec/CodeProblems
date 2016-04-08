#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave, Image

f = [wave.openfp('waves/lake%d.wav'%i,'rb') for i in range(1,26)]
# tous les .wav font 10800 frames en mono
nbframes = f[0].getnframes()

w = 60
h = nbframes/3/w
dst = Image.new('RGB',(5*w,5*h))
pix = dst.load()

for i in range(5):
    for j in range(5):
        n = 5*j+i
        dx = w*i
        dy = h*j
        for y in range(h):
            for x in range(w):
                pix[x+dx,y+dy] = (ord(f[n].readframes(1)),ord(f[n].readframes(1)),ord(f[n].readframes(1)))
        
for w in f:
    w.close()

dst.save('dst.png')
