#!/usr/bin/env python3

from collections import Counter

T = int(input())
for _ in range(T):
    S = Counter(input().strip())
    x,y = map(int,input().split())
    a,b = S['a'],S['b']
    ca,cb = 'a','b'
    if a<b:
        a,b = b,a
        ca,cb = cb,ca
        x,y = y,x
    res = []
    while a>0:
        if b==0:
            na = min(a,x)
            res.append(na*ca+('*' if a>x else ''))
            a -= na
        elif a==b:
            res.append(a*(ca+cb))
            a = b = 0
        else:
            na = min(a-b+1,x)
            res.append(na*ca+cb)
            a -= na
            b -= 1
    print(''.join(res))
