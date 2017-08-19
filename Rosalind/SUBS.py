#!/usr/bin/env python3

S = input()
T = input()
res = []
p = S.find(T)
while p!=-1:
    res.append(str(p+1))
    p = S.find(T,p+1)
print(' '.join(res))
