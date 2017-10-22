#!/usr/bin/env python3

n = int(input())
a = int(input())
b = int(input())
c = int(input())

mab = min(a,b)
res = (n-1)*mab
if n>1:
    res = min(res,mab+(n-2)*c)
print(res)
