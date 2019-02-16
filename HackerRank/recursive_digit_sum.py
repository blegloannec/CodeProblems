#!/usr/bin/env python3

n,k = input().split()
k = int(k)
s = sum(k*int(d) for d in n)
while s>=10:
    n,s = s,0
    while n>0:
        n,d = divmod(n,10)
        s += d
print(s)
