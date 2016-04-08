#!/usr/bin/env python

import urllib, Image, StringIO

o = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
i = Image.open(StringIO.StringIO(o.read()))
p = i.load()
w,h = i.size
print ''.join([chr(p[x,h/2][0]) for x in range(0,w-20,7)])

print ''.join(map(chr,[105, 110, 116, 101, 103, 114, 105, 116, 121]))
