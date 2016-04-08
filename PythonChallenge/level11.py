#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, Image, StringIO

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='inflate',uri=url,user='huge',passwd='file')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
img = Image.open(StringIO.StringIO(urllib2.urlopen(url).read()))
pix = img.load()
w,h = img.size
for x in range(w/2):
    for y in range(h/2):
        pix[x,y] = pix[2*x,2*y]
img.save('out.png')
