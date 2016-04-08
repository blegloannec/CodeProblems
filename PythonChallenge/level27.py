#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image, bz2

# Contrairement aux défis précédents, l'image est ici en 
# mode P, pour palette...
img = Image.open('zigzag.gif')

# Conversion en données brutes
imgL = img.copy().convert('L')


a = img.tostring()
b = imgL.tostring()
# On remarque que les données brutes très proches des 
# données codées. On fait le diff.
z = zip(a[1:],b[:-1])
diff = filter((lambda (x,y):x!=y), z)
print bz2.decompress(''.join(map((lambda (x,y):x),diff)))


## On affiche les point d'egalité pour un indice...
eq = map((lambda (x,y):x==y), z)
dst = Image.new('1',img.size)
dst.putdata(eq)
dst.save('out.gif')
