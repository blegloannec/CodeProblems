#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image

f = open('yankeedoodle.csv','r')
chaines = map(str.strip,f.read().split(','))
f.close()

# 7367 valeurs flottantes
# 7367 = 139 x 53
w,h = 139,53
img = Image.new('L',(w,h))
pix = img.load()
for x in range(w):
    for y in range(h):
        pix[x,y] = int(round(255*float(chaines[x*h+y])))
img.save('formule.png')

l = []
for i in range(0,len(chaines)-4,3):
    l.append(chr(int(chaines[i][5]+chaines[i+1][5]+chaines[i+2][6])))
print ''.join(l)[:200]
