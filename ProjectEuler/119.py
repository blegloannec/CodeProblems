#!/usr/bin/env python

def digits_sum(n,b=10):
    s = 0
    while n>0:
        s += n%b
        n /= b
    return s

def main():
    L = []
    for a in xrange(4,100):
        x = a
        for b in xrange(2,30):
            x *= a
            if digits_sum(x)==a:
                L.append(x)
    L.sort()
    print L[29]
                
main()
