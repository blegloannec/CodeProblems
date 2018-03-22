#!/usr/bin/env python3

P = 10**9+7

def inv_mod(x):
    return pow(x,P-2,P)

def binom(n,p):
    b = 1
    for i in range(p):
        b = (b*(n-i)*inv_mod(p-i))%P
    return b

def main():
    A = int(input())
    B = int(input())
    if B<A:
        A,B = B,A
    if A<24:
        res = 0 if B!=25 else binom(A+24,A)
    else:
        res = 0 if B!=A+2 else (pow(2,A-24,P)*binom(48,24))%P
    print(res)

main()
