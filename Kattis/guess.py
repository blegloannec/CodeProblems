#!/usr/bin/env python3

# Interactive!

import sys

l = 1; r = 1000
while True:
    m = (l+r)//2
    sys.stdout.write(f'{m}\n')
    sys.stdout.flush()
    res = sys.stdin.readline().strip()
    if res=='correct':
        break
    elif res=='lower':
        r = m-1
    else:
        l = m+1
