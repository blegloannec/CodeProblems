#!/usr/bin/env python

from math import *

# n = int(log10(x^n))+1 = int(n*log10(x))+1
# donc log10(x)<=1 donc x<=9
# et n-1 <= n*log10(x) donc n <= 1/(1-log10(x)) <= 21 (pour x=9)

def main():
    cpt = 0
    for x in xrange(1,10):
        for n in xrange(1,int(ceil(1/(1-log10(x))))+1):
            if int(n*log10(x))==n-1:
                cpt += 1
    print cpt

main()
