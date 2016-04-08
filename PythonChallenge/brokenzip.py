#!/usr/bin/env python

import hashlib

# zip inside zip from level 24
f = open('mybroken.zip','r')
z = f.read()
f.close()

# on corrige une erreur d'un octet
for i in range(len(z)):
    for o in range(256):
        zmod = z[:i]+chr(o)+z[i+1:]
        h = hashlib.md5(zmod).hexdigest()
        # hash from Leopold at level 23
        if h=='bbb8b499a0eef99b52c7f13f4e78c24b':
            f = open('myNOTbroken.zip','w')
            f.write(zmod)
            f.close()
            break
