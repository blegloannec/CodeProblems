#!/usr/bin/env python3

P = 10**9+7

def inv_mod(n,p=P):
    return pow(n,p-2,p)

# modular fast exponentiation
# using tan(a+b) = (tan(a)+tan(b)) / (1-tan(a)*tan(b))
def tan_mult_mod(t,n,p=P):
    if n==0:
        return 0
    t2 = (2*t*inv_mod(1-t*t)) % p
    if n%2==0:
        return tan_mult_mod(t2,n//2,p)
    else:
        t1 = tan_mult_mod(t2,n//2,p)
        return ((t+t1)*inv_mod(1-t*t1)) % p

def main():
    T = int(input())
    for _ in range(T):
        p,q,n = map(int,input().split())
        t = (p*inv_mod(q)) % P
        print(tan_mult_mod(t,n))

main()
