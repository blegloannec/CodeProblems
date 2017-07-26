#!/usr/bin/env python

from math import *
from fractions import gcd

# f(x) = (n/x)^x
# g(x) = ln(f(x)) = x*ln(n) - x*ln(x)
# g'(x) = ln(n) - ln(x) - 1
# g'(x0) = 0 <=> ln(x0) = ln(n)-1
# solution reelle x0 = exp(ln(n)-1) = n/e
# solution entiere int(x0) ou int(x0)+1
# en pratique, pour N>4, c'est en fait toujours round(x0)

def M(N):
    return int(round(N/e))

# la fraction p/q est "terminating" si son
# denominateur sous forme irreductible est
# de la forme 2^a.5^b
def term(p,q):
    q = q/gcd(p,q)
    while q%2==0:
        q /= 2
    while q%5==0:
        q /= 5
    return q==1

def main():
    S = [0,0,0,0,0]
    for n in xrange(5,1000001):
        k = M(n)
        # clairement n^k/k^k terminating <=> n/k terminating
        S.append(S[-1] + (-n if term(n,k) else n))
    Q = int(raw_input())
    for _ in xrange(Q):
        n = int(raw_input())
        print S[n]

main()
