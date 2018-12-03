#!/usr/bin/env python3

import sys, re
from collections import defaultdict

form = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
I = [tuple(map(int,form.match(L).groups())) for L in sys.stdin.readlines()]

# Part 1
D = defaultdict(int)
for _,x,y,w,h in I:
    for i in range(x,x+w):
        for j in range(y,y+h):
            D[i,j] += 1
print(sum(int(D[p]>1) for p in D))

# Part 2
for ID,x,y,w,h in I:
    if all(D[i,j]==1 for i in range(x,x+w) for j in range(y,y+h)):
        print(ID)
