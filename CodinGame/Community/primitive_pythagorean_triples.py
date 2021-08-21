#!/usr/bin/env python3

from math import gcd

def pythagorean(N):
    m = 2
    while m*m <= N:
        n = 1 + m%2
        while n < m and n*n+m*m <= N:
            if gcd(m,n) == 1:
                a,b,c = m*m-n*n, 2*m*n, m*m+n*n
                if a > b: a,b = b,a  # only to fit the statement
                yield (a,b,c)
            n += 2
        m += 1

N = int(input())
print(len(list(pythagorean(N))))
