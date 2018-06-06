#!/usr/bin/env python

import sys
import random
random.seed()

def fisher_yates(n):
    a = range(n)
    for k in xrange(n):
        p = random.randint(k,n-1)
        a[k],a[p] = a[p],a[k]
    return a

def bad_shuffle(n):
    a = range(n)
    for k in xrange(n):
        p = random.randint(0,n-1)
        a[k],a[p] = a[p],a[k]
    return a

def higher(a):
    s = 0
    for i in xrange(len(a)):
        if a[i]>=i:
            s += 1
    return s

def test():
    n = 1000
    t = 10000
    s1,s2 = 0,0
    for i in xrange(t):
        a = fisher_yates(n)
        s1 += higher(a)
        b = bad_shuffle(n)
        s2 += higher(b)
    print s1/t,s2/t

def verif():
    n = 1000
    t = 10000
    v = 0
    for i in xrange(t):
        good = random.choice([True, False])
        a = fisher_yates(n) if good else bad_shuffle(n)
        if (higher(a)<=514 and good) or (higher(a)>514 and not good):
            v += 1
    print float(v)/t
            
    
def main():
    T = int(sys.stdin.readline())
    for t in xrange(1,T+1):
        a = map(int,sys.stdin.readline().split())
        print 'Case #%d: %s' % (t, 'GOOD' if higher(a)<=514 else 'BAD')

#test()
# FY 500 (logique), BS 528

#verif()

main()
