#!/usr/bin/env python

import zipfile, re

z = zipfile.ZipFile('./channel.zip')
nothing = 90052
while True:
    f = str(nothing)+'.txt'
    print z.getinfo(f).comment,
    s = re.search(' [0-9]+$',z.open(f).read())
    if s==None:
        break
    nothing = int(s.group())
