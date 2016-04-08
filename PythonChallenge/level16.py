#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, Image, StringIO

url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='inflate',uri=url,user='huge',passwd='file')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
img = Image.open(StringIO.StringIO(urllib2.urlopen(url).read()))
pix = img.load()
w,h = img.size
dst = Image.new(img.mode,img.size)
dpix = dst.load()
for y in range(h):
    rose = [pix[x,y] for x in range(w)].index(195)
    for x in range(w):
        dpix[x,y] = pix[(x+rose)%w,y]
dst.save('out.gif')
