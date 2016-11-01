#!/usr/bin/env python

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

# generateur des diviseurs
def divisors(F,i=0):
    if i==len(F):
        yield 1
    else:
        p,m = F[i]
        f = 1
        for _ in xrange(m+1):
            for d in divisors(F,i+1):
                yield f*d
            f *= p

def digits_sum(n,b=10):
    s = 0
    while n>0:
        s += n%b
        n /= b
    return s

def digit_root(n):
    if n<10:
        return n
    return digit_root(digits_sum(n))

def main():
    N = 10**6
    _,D = sieve_decomp(N)
    s = 0
    DRS = [0 for _ in xrange(N)]
    for n in xrange(2,N):
        DRS[n] = digit_root(n)
        for d in divisors(D[n]):
            if 1<d<n:
                DRS[n] = max(DRS[n],DRS[n/d]+DRS[d])
        s += DRS[n]
    print s

main()
