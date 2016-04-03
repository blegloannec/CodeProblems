#!/usr/bin/env python

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def permut(N,C):
    res = []
    digits = range(N)
    for p in range(N-1,0,-1):
        f = fact(p)
        k = C/f
        res.append(digits[k])
        digits = digits[:k]+digits[k+1:]
        C -= k*f
    res.append(digits[0])
    return res

print ''.join(map(str,permut(9+1,1000000-1)))
