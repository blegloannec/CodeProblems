#!/usr/bin/env python3

import sys, re

I = [re.match(r'(.+)-(.+) (.): (.+)$', L.strip()) for L in sys.stdin.readlines()]
part1 = part2 = 0
for L in I:
    l = int(L.group(1))
    r = int(L.group(2))
    a = L.group(3)
    pwd = L.group(4)
    if l <= pwd.count(a) <= r:
        part1 += 1
    if (pwd[l-1]==a)+(pwd[r-1]==a) == 1:
        part2 += 1
print(part1)
print(part2)
