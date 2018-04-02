#!/usr/bin/env python3

import sys
from math import *

M = 10**6+1
L = 0.
D = [1]*M
for i in range(2,M):
    L += log10(i)
    D[i] = ceil(L)    

for L in sys.stdin.readlines():
    print(D[int(L)])
