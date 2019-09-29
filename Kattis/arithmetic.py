#!/usr/bin/env python3

# 4 octal digits = 12 bits = 3 hex digits

S = input()
if S=='0':
    print(0)
else:
    r = len(S)%4
    if r>0:
        S = '0'*(4-r) + S
    print(''.join('{:03X}'.format(int(S[i:i+4],8)) for i in range(0,len(S),4)).lstrip('0'))
