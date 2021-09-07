#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, gzip, cStringIO, difflib, binascii

url = 'http://www.pythonchallenge.com/pc/return/deltas.gz'

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='inflate',uri=url,user='huge',passwd='file')
opener = urllib2.build_opener(auth_handler)
deltas = gzip.GzipFile(fileobj=cStringIO.StringIO(opener.open(url).read())).read().splitlines()

left,right = [],[]

for l in deltas:
    left.append(l[:53])
    right.append(l[56:])


f = [open('out%d.png' % i, 'w') for i in range(3)]
d = {' ':0,'+':1,'-':2}
for l in difflib.ndiff(left,right):
    f[d[l[0]]].write(binascii.unhexlify(''.join(l[2:].split(' '))))
for ff in f:
    ff.close()
