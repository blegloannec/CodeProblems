#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='inflate',uri=url,user='huge',passwd='file')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
source = urllib2.urlopen(url)
f = []
for i in range(5):
    f.append(open('out%i' % i, 'w'))
c = source.read(1)
i = 0
while c!='':
    f[i].write(c)
    i = (i+1)%5
    c = source.read(1)
for a in f:
    a.close()

url = 'http://www.pythonchallenge.com/pc/return/evil4.jpg'
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='inflate',uri=url,user='huge',passwd='file')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
print urllib2.urlopen(url).read()
