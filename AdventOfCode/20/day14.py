#!/usr/bin/env python3

import sys

I = [L.strip().split(' = ') for L in sys.stdin.readlines()]


# Part 1
Mem = {}
for L,R in I:
    if L=='mask':
        mask = R
        mask_idx = int(mask.replace('0','1').replace('X','0'), 2)
        mask_val = int(mask.replace('X','0'), 2)
    else:
        addr = int(L[4:-1])
        val = int(R)
        Mem[addr] = (val ^ (val & mask_idx)) | mask_val
print(sum(Mem.values()))


# Part 2
Mem = {}
for L,R in I:
    if L=='mask':
        mask = R
        Xbit = [1<<i for i,x in enumerate(reversed(mask)) if x=='X']
        mask_1 = int(mask.replace('X','0'), 2)
    else:
        addr = int(L[4:-1]) | mask_1
        val = int(R)
        for p in range(1<<len(Xbit)):
            a = addr
            for i,b in enumerate(Xbit):
                if (p>>i)&1:
                    a ^= b
            Mem[a] = val
print(sum(Mem.values()))
