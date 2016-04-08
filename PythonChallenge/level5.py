#!/usr/bin/env python

import urllib, pickle

o = pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
for l in o:
    print ''.join(map((lambda (x,y):x*y),l))
