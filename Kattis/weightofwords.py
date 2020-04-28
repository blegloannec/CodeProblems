#!/usr/bin/env python3

let = lambda w: chr(w-1+ord('a'))

l,w = map(int,input().split())
if l<=w<=26*l:
    q,r = divmod(w,l)
    print(let(q)*(l-r) + let(q+1)*r)
else:
    print('impossible')
