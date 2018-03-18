#!/usr/bin/env python3

# http://oeis.org/A055388
# http://oeis.org/A002326

# for even n, the period is twice the multiplicative order of 4 mod odd n-1
# hence we need 4^30 = 1 mod n-1, i.e. n-1 | 2^60-1
# and 4^k =/= 1 mod n-1 for k < 30 = 2*3*5
# it is enough to check that for k = 30/2, 30/3 and 30/5

# primal decomposition of 2^60-1
D = [(3,2),(5,2),(7,1),(11,1),(13,1),(31,1),(41,1),(61,1),(151,1),(331,1),(1321,1)]

def divisors(F,i=0,d=1):
    if i==len(F):
        yield d
    else:
        p,m = F[i]
        f = 1
        for _ in range(m+1):
            yield from divisors(F,i+1,d*f)
            f *= p

s = 0
for d in divisors(D):
    if d>4 and all(pow(4,f,d)!=1 for f in [6,10,15]):
        s += d+1
print(s)
