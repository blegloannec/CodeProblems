#!/usr/bin/env python

import sys

P = 1000000007

# Formule "naive" :
# for n in xrange(3,N+1,2):
#     s += n*n + n*n-(n-1) + n*n-2*(n-1) + n*n-3*(n-1)
# soit : sum(4(2n+1)^2 - 6(2n), n=1..(N-1)/2)
# a simplifier pour obtenir la formule dans le code ci-dessous 

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        n = (N-1)/2
        s = 1 + 8*n*(n+1)*(2*n+1)/3 + 2*n*(n+1) + 4*n
        print s%P

main()
