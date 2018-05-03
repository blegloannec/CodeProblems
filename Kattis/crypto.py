#!/usr/bin/env python3

def decomp(n):
    F = []
    m = 0
    while n%2==0:
        n /= 2
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    while n>1 and i*i<=n:
        m = 0
        while n%i==0:
            n /= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

def main():
    N = int(input())
    D = decomp(N)
    M = 0
    for p,m in D:
        if m>M:
            M = m
            K = p
    print(K)

main()
