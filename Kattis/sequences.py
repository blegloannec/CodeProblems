#!/usr/bin/env python3

import sys

P = 10**9+7

# for one given sequence:
#   seq  11010
#   #1s  12233  +1   at each 1
#   inv  00225  +#1s at each 0
# we simply generalize this for all sequences at the same time

S = sys.stdin.readline().strip()
res = cnt_1 = 0
cnt_seq = 1
for c in S:
    if c=='1':
        cnt_1 = (cnt_1 + cnt_seq) % P
    elif c=='0':
        res = (res + cnt_1) % P
    else:
        res = (2*res + cnt_1) % P
        cnt_1 = (2*cnt_1 + cnt_seq) % P
        cnt_seq = (2*cnt_seq) % P
print(res)
