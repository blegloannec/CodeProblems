#!/usr/bin/env python

import random
random.seed()

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=15):
    if n<2:
        return False
    b = digits(n-1,2)
    for j in xrange(s):
        if witness(random.randint(1,n-1),n,b):
            return False
    return True

M = 10**14
def gen(n,s,strong=False):
    if n<M:
        if n%s==0:
            strong = miller_rabin(n/s)
            for c in xrange(10):
                for h in gen(10*n+c,s+c,strong):
                    yield h
        elif strong and miller_rabin(n):
            yield n

print sum(sum(gen(i,i)) for i in xrange(1,10))
