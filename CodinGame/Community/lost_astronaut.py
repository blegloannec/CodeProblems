#!/usr/bin/env python3

import re

N = int(input())
M = re.findall(r'(.+?) ', input()+' ')
assert len(M)==N

O = []
for c in M:
    if len(c)==1:
        o = c
    elif len(c)==2 and c!='40':
        o = chr(int(c, 16))
    elif len(c)<=3:
        o = chr(int(c, 8))
    else:
        o = chr(int(c, 2))
    O.append(o)
print(''.join(O))
