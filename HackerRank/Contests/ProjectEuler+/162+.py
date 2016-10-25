#!/usr/bin/env python

import sys

def cpt(n):
    aucun = 13**n
    pas0 = 15**n
    pas1 = pasA = 14*15**(n-1)
    pas1A = 13*14**(n-1)
    pas01 = pas0A = 14**n
    tous = 15*16**(n-1)
    # inclusion-exclusion
    return tous - (pas0+pas1+pas1) + (pas1A+pas01+pas0A) - aucun

n = int(sys.stdin.readline())
print sum(cpt(i) for i in xrange(3,n+1))%(10**9+7)
