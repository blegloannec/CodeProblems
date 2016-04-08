#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image
from math import sqrt

img = Image.open('beer2.png','r')
data = img.tostring()

# Comme indiqué dans l'indice, on applique un seuil sur l'image,
# on rééquilibre les couleurs et on met ça sous forme carrée.
tailles = set()
for s in range(1,255):
    d = filter(lambda x:ord(x)<=s, data)
    t = len(d)
    r = int(sqrt(t))
    if r**2==t and not t in tailles:
        tailles.add(t)
        #print r, t
        dst = Image.new('L',(r,r))
        dst.putdata(map(lambda x:ord(x)*255/s,d))
        dst.save('beer%d.png'%r)

print 'Les lettres entourées dans les images forment le mot "gremlins" !'
