#!/usr/bin/env python

# JA(n) = sum(1/k * binom(n,k)/2^n, k=1..n)
#       = sum(1/k * binom(n,k), k=1..n) / 2^n
# on a (x+1)^n = sum(binom(n,k)*x^k, k=0..n)
# donc ((x+1)^n - 1) / x = sum(binom(n,k)*x^(k-1), k=1..n)
# or ((x+1)^n - 1) / x = sum((x+1)^k, k=0..n-1)
# on integre des 2 cotes (attention a la constante)
# sum(1/(k+1) * (x+1)^(k+1), k=0..n-1) + K = sum(1/k * binom(n,k)*x^k, k=1..n)
# ou K = sum(1/(k+1) * (0+1)^(k+1), k=0..n-1) = H(n) (serie harmonique)
# on evalue en x = 1
# sum(2^k / k, k=1..n) - H(n) = 2^n * JA(n)

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

def JA(n):
    return sum(1./k*binom(n,k) for k in xrange(1,n+1)) / 2.**n

def JAbis(n):
    H = sum(1./k for k in xrange(1,n+1))
    return (sum(2.**k/k for k in xrange(1,n+1))-H) / 2.**n

def JB(n):
    return sum(1./(k*binom(n,k)) for k in xrange(1,n+1))

def JBbis(n):
    return sum(2.**k/k for k in xrange(1,n+1)) / 2.**n

def S(m):
    res = 0
    J,H = 0,0
    for n in xrange(1,m+1):
        H = H/2. + (1./(n*2**n) if n<1000 else 0.)
        J = J/2. + 1./n
        res += 2*J - H
    return res

print S(123456789)
