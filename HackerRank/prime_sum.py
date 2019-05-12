#!/usr/bin/env python3

# Miller-Rabin (64-bit deterministic)
def witness(a,n,b):
    d = 1
    for i in range(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n):
    if n<2:
        return False
    m = n-1
    b = []
    while m:
        b.append(m&1)
        m >>= 1
    for w in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if w%n!=0 and witness(w,n,b):
            return False
    return True

# Goldbach conjecture:
#  (1) Every even integer > 2 can be written as the sum of 2 primes.
#  (2) Every integer > 5 can be written as the sum of 3 primes.

def prime_sum(N,K):
    if N<2*K:
        return False
    elif K==1:
        return miller_rabin(N)
    elif N%2==0 or K>=3:
        # if N even and K >= 2,
        #   if N = 2K, obvious solution
        #   else N = 2(K-2) + M where M even > 4, then Goldbach (1) on M
        # if N odd and K >= 3,
        #   N = 2(K-3) + M where M odd > 6, then Goldbach (2) on M
        return True
    else:
        # N odd and K = 2
        # as 2 is the only even prime, we must have N = 2 + M with M prime
        return miller_rabin(N-2)

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        print('Yes' if prime_sum(N,K) else 'No')
