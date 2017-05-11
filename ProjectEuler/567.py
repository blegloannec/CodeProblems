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

# JB(n) = sum(1/(k*binom(n,k)), k=1..n)
# et l'on remarque un peu par hasard (!) que
# JB(n) = sum(2^k / k, k=1..n) / 2^n (= JA(n) + H(n)/2^n)
# ce qui n'est pas evident a demontrer...
# (voir le post de amic sur le forum du pb 568 pour une
#  preuve simple et elegante)

def S(m):
    res,J,H,p2 = 0,0,0,1.
    for n in xrange(1,m+1):
        p2 *= 2.
        H = H/2. + 1./(n*p2)
        J = J/2. + 1./n
        res += 2*J - H
    return res

print S(123456789)
