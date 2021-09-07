#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, Image, StringIO

url = 'http://www.pythonchallenge.com/pc/return/wire.png'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='inflate',uri=url,user='huge',passwd='file')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
img = Image.open(StringIO.StringIO(urllib2.urlopen(url).read()))
pix = img.load()
print img.size

dst = Image.new(img.mode,(100,100))
dpix = dst.load()

x,y = -1,0
c = 0
n = 100
while n>1:
    for i in range(n):
        x+=1
        dpix[x,y] = pix[c,0]
        c+=1
    for i in range(n-1):
        y+=1
        dpix[x,y] = pix[c,0]
        c+=1
    for i in range(n-1):
        x-=1
        dpix[x,y] = pix[c,0]
        c+=1
    for i in range(n-2):
        y-=1
        dpix[x,y] = pix[c,0]
        c+=1
    n-=2

dst.save('out.png')
