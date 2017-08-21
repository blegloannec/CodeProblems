#!/usr/bin/env python3

import sys

# that one is pretty stupid...

L = sys.stdin.readlines()
n = int(L[0])
m = len(L)-1
print(n-1-m)
