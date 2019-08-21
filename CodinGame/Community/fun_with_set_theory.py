#!/usr/bin/env python3

import re

E = input().replace(';',',').replace('U','|').replace('I','&')
B = (('[',''),(']','+1'))
for l,i in B:
    for r,j in B:
        E = re.sub(r'\%s(-?[0-9]+),(-?[0-9]+)\%s'%(l,r), r'set(range(\1%s,\2%s))'%(i,j), E)
S = eval(E)
if S: print(*sorted(S))
else: print('EMPTY')
