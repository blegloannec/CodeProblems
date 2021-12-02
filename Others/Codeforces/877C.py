#!/usr/bin/env python3

from itertools import chain

n = int(input())
print(n+n//2)
print(' '.join(map(str,chain(range(2,n+1,2),range(1,n+1,2),range(2,n+1,2)))))
