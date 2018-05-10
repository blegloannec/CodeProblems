#!/usr/bin/env pypy

# runs in ~10s with pypy (full decomp sieve takes ~6s)

def sieve_decomp(N):
    P = [True]*N
    Decomp = [[] for _ in xrange(N)]
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

# subtract decomposition D2 from decomposition D1 (~division)
def decomp_sub(D1,D2):
    D = []
    i = 0
    for (p,m) in D1:
        if i<len(D2):
            q,n = D2[i]
            if q<p:      # D1 not divisible by D2
                return None
            if q==p:
                if n>m:  # D1 not divisible by D2
                    return None
                m -= n
                i += 1
        if m>0:
            D.append((p,m))
    return D if i==len(D2) else None

# returns (the unique) n such that phi(n^2) = t or 0 if no solution
# as all prime factors in n^2 appear at least twice, this is completely
# deterministic: the largest prime factor p in t is also the one in n
# so we can repeat the process after removing it and dividing by p-1...
def inv_euler_square(D,T):
    n = 1
    while T:
        p,m = T.pop()  # largest prime factor
        if m%2==0:     # val_p(n^2) = m+1 even
            return 0
        T = decomp_sub(T,D[p-1])
        if T==None:    # T not divisible by p-1
            return 0
        n *= p**((m+1)//2)
    return n

def S(N):
    M = int((N*N)**(1./3.))
    _,D = sieve_decomp(M+1)
    k = 2
    res = 0
    while k<=M:
        T = [(p,3*m) for (p,m)  in D[k]]
        n = inv_euler_square(D,T)
        if n<N:
            res += n
        k += 1
    return res

print S(10**10)
