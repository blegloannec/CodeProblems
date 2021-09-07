#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, Image, cStringIO, zlib

url = 'http://www.pythonchallenge.com/pc/hex/maze.png'
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='pluses and minuses',uri=url,user='butter',passwd='fly')
opener = urllib2.build_opener(auth_handler)

img = Image.open(cStringIO.StringIO(opener.open(url).read()))
#img = Image.open('maze.png')
w,h = img.size
pix = img.load()
blanc = (255,255,255,255)
bleu = (0,0,255,255)
forb = [blanc,bleu]

dist = [[-1 for x in range(w)] for y in range(h)]
fil = [(w-1,0)]
dist[w-1][0] = 0
while fil!=[]:
    x,y = fil[0]
    fil = fil[1:]
    if y==h-1:
        break
    if dist[x][y]>0:
        pass
    d = dist[x][y]
    if x<w-1 and pix[x+1,y]!=blanc and dist[x+1][y]<0:
        dist[x+1][y] = d+1
        fil.append((x+1,y))
    if x>0 and pix[x-1,y]!=blanc and dist[x-1][y]<0:
        dist[x-1][y] = d+1
        fil.append((x-1,y))
    if y>0 and pix[x,y-1]!=blanc and dist[x][y-1]<0:
        dist[x][y-1] = d+1
        fil.append((x,y-1))
    if y<h-1 and pix[x,y+1]!=blanc and dist[x][y+1]<0:
        dist[x][y+1] = d+1
        fil.append((x,y+1))

d = dist[x][y]
l = []
while d>=0:
    if x%2==1 and y%2==1:
        l.append(chr(pix[x,y][0]))
    pix[x,y] = bleu
    if x<w-1 and pix[x+1,y]!=blanc and dist[x+1][y]==d-1:
        x += 1
    elif x>0 and pix[x-1,y]!=blanc and dist[x-1][y]==d-1:
        x -= 1
    elif y>0 and pix[x,y-1]!=blanc and dist[x][y-1]==d-1:
        y -= 1
    elif y<h-1 and pix[x,y+1]!=blanc and dist[x][y+1]==d-1:
        y += 1
    d -= 1

img.save('out.png')
f = open('out.zip','w')
f.write(''.join(l[::-1]))
f.close()
