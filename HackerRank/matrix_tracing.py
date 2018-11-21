#!/usr/bin/env python3

P = 10**9+7

# factorial mod
N = 2*10**6
F = [1]*N
for n in range(2,N):
    F[n] = (n*F[n-1]) % P

def inv(n):
    return pow(n,P-2,P)

def binom(n,p):
    return (F[n]*inv(F[p])*inv(F[n-p])) % P

def main():
    T = int(input())
    for _ in range(T):
        m,n = map(int,input().split())
        print(binom(n+m-2,n-1))

main()
