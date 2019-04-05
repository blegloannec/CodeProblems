#!/usr/bin/env python3

MOD = 1000003  # prime

# the required results can be computed (inefficiently) with the following DP
memo = {}
def poly(n, k, loop=False):
    if k==0:
        return 1
    if k>=n-1-int(loop):
        return 0
    if n<=2+int(loop):
        return 0
    if (n,k,loop) in memo:
        return memo[n,k,loop]
    res = poly(n-1,k)
    for m in range(2,n-int(loop)):
        for l in range(k):
            res += poly(m+1,l,True) * poly(n-m,k-1-l)
            res %= MOD
    memo[n,k,loop] = res
    return res

# which allows to derive the following formulas:
# http://oeis.org/A033282  (for loops)
# http://oeis.org/A088617

# apparently (according to the editorial), the problem mostly consisted in
# computing this formula (considered itself as prerequisite knowledge)
def inv(x):
    return pow(x, MOD-2, MOD)

# modular factorials up to MOD
Fact = [1]*MOD
for i in range(2,MOD):
    Fact[i] = (i*Fact[i-1]) % MOD

# for larger n, n! = A * MOD^v
# where v is computed by the following (Legendre's formula)...
def fact_val(n):
    q = MOD
    v = 0
    while q<=n:
        v += n//q
        q *= MOD
    return v

# ...and A is relatively easily given by the following computation
# (it's easy to miss the fact(q) factor though, which comes from the
#  multiples of MOD in the n! product)
def fact(n):
    if n<MOD:
        return Fact[n]
    q,r = divmod(n,MOD)
    return (pow(Fact[MOD-1],q,MOD) * fact(q) * Fact[r]) % MOD

# modular binomial in the form A * MOD^v
def binom(n,p):
    assert 0<=p<=n
    A = (fact(n)*inv(fact(p))*inv(fact(n-p))) % MOD
    v = fact_val(n) - fact_val(p) - fact_val(n-p)
    return (A,v)

# formula binom(n+k+2,k)*binom(n,k)/(k+1)
def form(n,k):
    n -= 3
    if k>n:
        return 0
    A1,v1 = binom(n+k+2,k)
    A2,v2 = binom(n,k)
    v3 = 0
    K = k+1
    while K%MOD==0:
        v3 += 1
        K //= MOD
    if v1+v2-v3>0:
        return 0
    return (A1*A2*inv(K)) % MOD

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        print(form(N,K))
