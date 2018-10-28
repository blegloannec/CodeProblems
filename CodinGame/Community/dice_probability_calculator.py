#!/usr/bin/env python3

from itertools import product
from collections import defaultdict

E = input().split('d')
V = defaultdict(int)
for X in product(*(range(1,int(E[i][0])+1) for i in range(1,len(E)))):
    V[eval(E[0]+''.join(str(X[i-1])+E[i][1:] for i in range(1,len(E))))] += 1
S = sum(V[x] for x in V)
for x in sorted(V):
    print('%d %.2f' % (x,100*V[x]/S))
