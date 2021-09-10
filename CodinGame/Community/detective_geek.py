#!/usr/bin/env python3

M = ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
print('%02d:%02d' % divmod(int(input().replace('*','0').replace('#','1'), 2), 100))
print(''.join(chr(12*M.index(w[:3])+M.index(w[3:])) for w in input().split()))
