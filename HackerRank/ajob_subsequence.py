#!/usr/bin/env python3

# We "simply" have to compute
#   sum_{n=K..N} binom(n,K) = sum_{n=0..N} binom(n,K)
#                           = binom(N+1,K+1)
# known as the hockey-stick identity
# https://en.wikipedia.org/wiki/Hockey-stick_identity

# Method 1: "huge parameters" modular fact/binomial computation
# See also ajob_subsequence_bis.py for an alternative approach
# (based on Lucas's theorem).

def inv(n):
    return pow(n,P-2,P)

# n! = A * P^v
# where v is computed by the following (Legendre's formula)...
def fact_val(n):
    q = P
    v = 0
    while q<=n:
        v += n//q
        q *= P
    return v

# ...and A is relatively easily given by the following computation
# (it's easy to miss the fact(q) factor though, which comes from the
#  multiples of P in the n! product)
def fact(n):
    if n<P:
        return Fact[n]
    q,r = divmod(n,P)
    return (pow(Fact[P-1],q,P) * fact(q) * Fact[r]) % P

# modular binomial in the form A * P^v
def binom(n,p):
    assert 0<=p<=n
    A = (fact(n) * inv((fact(p)*fact(n-p))%P)) % P
    v = fact_val(n) - fact_val(p) - fact_val(n-p)
    return 0 if v>0 else A

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N,K,P = map(int,input().split())
        Fact = [1]*P
        for i in range(2,P):
            Fact[i] = (Fact[i-1]*i) % P
        print(binom(N+1,K+1))
