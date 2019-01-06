#!/usr/bin/env python3

# simple precomp
F = [1]*10
for i in range(1,len(F)):
    if i%2==0 or i%5==0:  # we ignore multiples of 2 or 5
        F[i] = F[i-1]
    else:
        F[i] = (F[i-1]*i) % 10

# contrib(n) = last digit of the product of the
#              odd numbers not divisible by 5 up to n
def contrib(n):
    q,r = divmod(n,10)
    return (pow(F[9],q,10)*F[r]) % 10

def legendre(n,p):
    v = 0
    q = p
    while q<=n:
        v += n//q
        q *= p
    return v

def fact_last_non0_digit(n):
    p2 = legendre(n,2)-legendre(n,5)
    d = pow(2,p2,10)
    a = 1
    while a<=n:
        b = a
        while b<=n:
            d = (d*contrib(n//b)) % 10
            b *= 5
        a *= 2
    return d

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(fact_last_non0_digit(N))
