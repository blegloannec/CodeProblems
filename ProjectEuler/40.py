#!/usr/bin/env python

def digit(n):
    d = 1
    p = 1
    while n>=9*d*p:
        n -= 9*d*p
        d += 1
        p *= 10
    k = p+n/d
    D = []
    while k>0:
        D.append(k%10)
        k /= 10
    return D[-1-(n%d)]

def main():
    res = 1
    for i in xrange(7):
        res *= digit((10**i)-1)
    print res

main()
