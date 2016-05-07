#!/usr/bin/env python

import sys,random
random.seed()

def digits(n,b):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

# Miller-Rabin
def witness(a,n):
    b = digits(n-1,2)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

def main():
    N = int(sys.stdin.readline())
    n = 3
    nb = 3
    while 100*nb>=N*(2*n-1):
        n += 2
        # seulement 4 tests pour que ca passe en temps
        if miller_rabin(n*n-(n-1),4):
            nb += 1
        if miller_rabin(n*n-2*(n-1),4):
            nb += 1
        if miller_rabin(n*n-3*(n-1),4):
            nb += 1
    print n

main()
