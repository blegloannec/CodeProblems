#!/usr/bin/env python3

import sys

input()
S = eval('["'+sys.stdin.read().replace('(','",["').replace(')','"],"').replace('|','","').replace('\n','\\n')+'"]')
c = 0
for i in range(len(S)):
    if isinstance(S[i],list):
        S[i] = S[i][c%len(S[i])]
        c += 1
print(''.join(S))
