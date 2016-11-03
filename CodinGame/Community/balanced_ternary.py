#!/usr/bin/env python3

dec = int(input())

D = {0:'T',1:'0',2:'1'}

K = (3**10-1)//2
n = dec+K
res = []
while n>0:
    res.append(D[(n%3)])
    n //= 3
while res and res[-1]=='0':
    res.pop()
if res:
    print(''.join(res[::-1]))
else:
    print(0)
