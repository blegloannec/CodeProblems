#!/usr/bin/env python

def digits(b,n):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def pal(l):
    return l==l[::-1]

def problem36():
    res = 0
    for n in range(1000000):
        if pal(digits(10,n)) and pal(digits(2,n)):
            res += n
    print res

problem36()
