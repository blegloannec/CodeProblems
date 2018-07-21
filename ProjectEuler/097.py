#!/usr/bin/env python

def expmod(x,n,p):
    if n==0:
        return 1
    elif n%2==0:
        return expmod((x*x)%p,n/2,p)
    return (x*expmod((x*x)%p,(n-1)/2,p))%p

M = 10000000000
print (28433*expmod(2,7830457,M)+1)%M
