#!/usr/bin/env python3

p,d,m,s = map(int,input().split())
cpt = 0
while s>=p:
    cpt += 1
    s -= p
    p = max(p-d,m)
print(cpt)
