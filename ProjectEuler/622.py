#!/usr/bin/env python3

# http://oeis.org/A055388
# http://oeis.org/A002326

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
