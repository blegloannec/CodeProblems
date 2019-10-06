#!/usr/bin/env python3

from fractions import Fraction

def digits3(p,q):
    assert 0<=p<=q
    t = 0
    seen = {}
    D = []
    while p not in seen:
        seen[p] = t
        a,p = divmod(3*p,q)
        D.append(a)
        t += 1
    t = seen[p]
    return D[:t],D[t:]

def main():
    while True:
        L = input()
        if L=='END':
            break
        x = Fraction(L)
        Pre,Per = digits3(x.numerator, x.denominator)
        if Pre and Per==[0]:
            # we get rid of the last non-0 digit
            # as 0.[..]1 = 0.[..]0222..
           Pre.pop() 
        member = all(d!=1 for d in Per+Pre)
        print('MEMBER' if member else 'NON-MEMBER')

main()
