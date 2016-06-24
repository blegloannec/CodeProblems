#!/usr/bin/env python

import sys
from math import sqrt

# generateur de palindromes
def gen_pal(n,a0=1):
    if n==0:
        yield 0
    elif n==1:
        for a in xrange(a0,10):
            yield a
    else:
        for a in xrange(a0,10):
            for x in gen_pal(n-2,0):
                yield 10*x+a+a*10**(n-1)

# test le plus rapide en python (si, si) !
# mais pas assez rapide pour ce pb
def is_palindrome(n):
    s = str(n)
    return s[::-1]==s

def main():
    # on stocke les palindromes pour test efficace
    P = set()
    for i in xrange(1,10):
        for p in gen_pal(i):
            P.add(p)
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        M,d = map(int,sys.stdin.readline().split())
        N = int(sqrt(M))+1
        # some numbers (actually only 2) can be obtained as several sums
        U = set()
        for i in xrange(1,N):
            s = i*i
            for j in xrange(i+d,N,d):
                s += j*j
                if s>=M:
                    break
                if s in P:
                    U.add(s)
        print sum(U)

main()
