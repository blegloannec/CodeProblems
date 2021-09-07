#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, bz2

url = 'http://www.pythonchallenge.com/pc/ring/guido.html'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='the order matters',uri=url,user='repeat',passwd='switch')
opener = urllib2.build_opener(auth_handler)
silence = opener.open(url).readlines()[12:]
print bz2.decompress(''.join(map(lambda l:chr(len(l)-1), silence)))
