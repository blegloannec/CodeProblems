#!/usr/bin/env python

def sieve(n):
    P = [True for _ in xrange(n)]
    Rad = [1 for _ in xrange(n)]
    for i in xrange(2,n,1):
        if P[i]:
            Rad[i] = i
            for j in xrange(2*i,n,i):
                Rad[j] *= i
                P[j] = False
    return Rad
                

def main():
    Rad = sieve(100001)
    l = sorted([(Rad[i],i) for i in xrange(1,len(Rad))])
    print l[9999][1]
    
main()
