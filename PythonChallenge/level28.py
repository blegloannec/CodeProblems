#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image

img = Image.open('bell.png')
w,h = img.size
pix = img.load()

## On voit facilement que le channel vert est brouillé
## Les autres sont propres.
#dst = Image.new('L',img.size)
vertdata = img.tostring()[1::3] # on extrait le vert
#dst.putdata(vertdata)
#dst.save('vert.png')

vd = map(ord,vertdata)
# On les traite par paires
paires = zip(vd[0::2],vd[1::2])
# On remarque que pour la plupart des paires, la différence est +/-42
# diff = map(lambda (x,y):x-y, paires)

# On affiche les paires pour lesquelles ce n'est pas le cas
print ''.join(map((lambda (x,y): chr(abs(x-y))), filter((lambda (x,y): abs(x-y)!=42), paires)))
whodunnit = 'Guido van Rossum'
print 'Createur de Python :', whodunnit
print 'Solution :',  whodunnit.split()[0]
