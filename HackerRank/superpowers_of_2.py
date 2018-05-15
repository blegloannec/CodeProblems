#!/usr/bin/env python3

# NB: for such reasonably small inputs, a solution such as
# pow(2,pow(2,a),b) is actually good enough

# better approach: use Euler's theorem and chinese remainders
# if b is odd, i.e. coprime with 2, then the answer is
# pow(2,pow(2,a,euler_phi(b)),b)
# else b = 2^k * c with odd c and we set
# x = 2^2^a mod 2^k and y = 2^2^a mod c
# we compute x and y and deduce 2^2^a mod b using chinese remainders
# we have y = pow(2,pow(2,a,euler_phi(c)),c)  (same as odd b)
# and x = 0                 if 2^a>=k, i.e. a>=log2(k)
#         pow(2,2**a,2**k)  otherwise

from math import log2

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def eulerphi_odd(n):
    assert(n&1)
    phi = 1
    i = 3
    while n>1 and i*i<=n:
        m = 0
        while n%i==0:
            n //= i
            m += 1
        if m>0:
            phi *= (i-1)*i**(m-1)
        i += 2
    if n>1:
        phi *= n-1
    return phi

def two_two_a_mod_b(a,b):
    if b&1:
        return pow(2,pow(2,a,eulerphi_odd(b)),b)
    else:
        k = 0
        c = b
        while c&1==0:
            c >>= 1
            k += 1
        tk = 1<<k
        x = 0 if a>=log2(k) else pow(2,1<<a,tk)
        y = pow(2,pow(2,a,eulerphi_odd(c)),c)
        return rev_chinois(x,tk,y,c)

a,b = map(int,input().split())
print(two_two_a_mod_b(a,b))
