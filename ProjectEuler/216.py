#!/usr/bin/env python

import random
random.seed()

# well, stupid algo here, obviously slow...

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

# Miller-Rabin
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

def main():
    cpt = 0
    for n in xrange(2,50000001):
        if miller_rabin(2*n*n-1,5):
            cpt += 1
    print cpt

main()
