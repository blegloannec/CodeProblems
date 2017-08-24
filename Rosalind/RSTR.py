#!/usr/bin/env python3

from collections import Counter

N,x = input().split()
N,x = int(N),float(x)
S = input()
C = Counter(S)
PS = (x/2)**(C['C']+C['G']) * ((1-x)/2)**(C['A']+C['T'])
P = 1-(1-PS)**N
print(P)
