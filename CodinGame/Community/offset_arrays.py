#!/usr/bin/env python3

import re

for _ in range(int(input())):
    t,l,r,v = re.fullmatch(r'(\w+)\[(-?\d+)\.\.(-?\d+)\] = (.+)', input()).groups()
    globals()[t] = dict(zip(range(int(l), int(r)+1), map(int, v.split())))
print(eval(input()))
