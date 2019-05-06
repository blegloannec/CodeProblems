#!/usr/bin/env python3

# Yet another repunit problem
# https://en.wikipedia.org/wiki/Repunit
# see also PE 129, 132 & 133

# Given X, let Y be the smallest integer such that
# X*Y = 44..400..0 = 4 * 11..1 * 10^b = 2^(b+2) * 5^b * 11..1
# Y is not divisible by 10 (otherwise Y/10 gives a smaller solution)
# Let us write X = 2^v2 * 5^v5 * x with x coprime with 2 and 5
#              Y = 2^w2 * 5^w5 * y (w2 and w5 not both positive)
# As 11..1 (a times) is not a multiple of 5 or 2, then, optimally
# if v2 = v5 + 2, we take b = w2 = w5 = 0
#    v2 > v5 + 2,         b = v2-2, w2 = 0, w5 = b-v5
#    v2 < v5 + 2,         b = v5, w2 = b+2-v2, w5 = 0
# Then we have x*y = 11..1 = (10^a - 1) / 9  (repunit)
# Hence 10^a = 1 mod 9x, a is the order of 10 mod 9x

# O(sqrt(N)) per query

from fractions import gcd

def decomp(n):
    F = []
    m = 0
    while n&1==0:
        n >>= 1
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    while n>1 and i*i<=n:
        m = 0
        while n%i==0:
            n //= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

def lcm(a,b):
    return a*b//gcd(a,b)

def eulerphi(n):
    phi = n
    for p,_ in decomp(n):
        phi = (p-1)*phi//p
    return phi

def multiplicative_order(G,N):
    assert gcd(G,N)==1
    Phi = eulerphi(N)
    D = decomp(Phi)
    o = 1
    for Q,M in D:
        G0 = pow(G,Phi//Q**M,N)
        o0 = 1
        while G0!=1:
            G0 = pow(G0,Q,N)
            o0 *= Q
        o = lcm(o,o0)
    return o

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        X = int(input())
        v2 = 0
        while X%2==0:
            v2 += 1
            X //= 2
        v5 = 0
        while X%5==0:
            v5 += 1
            X //= 5
        b = max(v2-2,v5)
        a = multiplicative_order(10,9*X)
        print(2*a+b)
