#!/usr/bin/env python3

# naive solution for verification purposes

def legendre(n,p):
    v = 0
    q = p
    while q<=n:
        v += n//q
        q *= p
    return v

def naive(n):  # en O(n)
    p2 = legendre(n,2)-legendre(n,5)
    k = pow(2,p2,10)
    for i in range(2,n+1):
        for p in [2,5]:
            while i%p==0:
                i //= p
        k = (k*i)%10
    return k

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(naive(N))
