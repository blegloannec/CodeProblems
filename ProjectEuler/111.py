#!/usr/bin/env python

import random
random.seed()

# generate all n-digit numbers (no leading 0) containing
# exactly k times the digit d
def gen(n,d,k):
    if n==0:
        if k==0:
            yield 0
    else:
        if k>0 and not (d==0 and n==1):
            for x in gen(n-1,d,k-1):
                yield 10*x+d
        if k<n:
            a0 = 0 if n>1 else 1
            for x in gen(n-1,d,k):
                for a in xrange(a0,10):
                    if a==d:
                        continue
                    yield 10*x+a

# Miller-Rabin
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
    b = digits(n-1,2)
    for j in xrange(s):
        if witness(random.randint(1,n-1),n,b):
            return False
    return True

# Main
def main():
    N = 10
    s = 0
    for d in xrange(10):
        s0 = 0
        k = N
        while s0==0:
            for x in gen(N,d,k):
                if miller_rabin(x):
                    s0 += x
            k -= 1
        s += s0
    print s

main()
