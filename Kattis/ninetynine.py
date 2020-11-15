#!/usr/bin/env python3

# Interactive problem!
# Clearly 97-98 are W, then 96 is L, then 94-95 are W, etc...
# A pos. p is losing iff p = 0 mod 3

import sys, random
random.seed()

i = 0
while i<99:
    r = i%3
    if r==0: i += random.randint(1,2)
    else:    i += 3-r
    sys.stdout.write(f'{i}\n')
    sys.stdout.flush()
    if i<99: i = int(sys.stdin.readline())
