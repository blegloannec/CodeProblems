#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile, zlib, bz2

## Archive obtenue au niveau 20
z = zipfile.ZipFile('./level21.zip','r')
z.setpassword('redavni')
print 'Files in archive:', z.namelist()
print
print 'readme.txt:'
print z.read('readme.txt')
buf = z.read('package.pack')
z.close()

Z = True
c = 0
l = []
ll = 0
oldl = 0
while True:
    ## On essaye de décompresser autant que possible en zlib ou bz2...
    try:
        oldbuf = buf
        if Z:
            buf = zlib.decompress(buf)
            l.append(' ')
        else:
            buf = bz2.decompress(buf)
            l.append('#')
    except:
        if ll<len(l):
            Z = not Z
            ll = len(l)
        elif oldl<len(l):
            ## Quand on ne sait plus quoi faire, on retourne le fichier !
            buf = buf[::-1]
            l.append('\n')
            oldl = len(l)
        else:
            break

print
print 'Final content of the pack:', oldbuf
print
print ''.join(l)

