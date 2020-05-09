#!/usr/bin/env python3

import sys

def fact_val(n,p):  # p-valuation de n!
    cpt = 0
    q = p
    while q<=n:
        cpt += n//q
        q *= p
    return cpt

def decomp(n):
    m = 0
    while n&1==0:
        n >>= 1
        m += 1
    if m>0:
        yield (2,m)
    i = 3
    while i*i<=n:
        m = 0
        while n%i==0:
            n //= i
            m += 1
        if m>0:
            yield (i,m)
        i += 2
    if n>1:
        yield (n,1)

def div_fact(m, n):
    if m==0:
        return False
    if m<=n:
        return True
    return all(fact_val(n,p)>=a for p,a in decomp(m))

def main():
    for L in sys.stdin.readlines():
        n,m = map(int, L.split())
        out = 'divides' if div_fact(m, n) else 'does not divide'
        sys.stdout.write(f'{m} {out} {n}!\n')

main()
