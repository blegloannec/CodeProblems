#!/usr/bin/env python

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def somme_chiffres10(n):
    return sum(chiffres10(n))

def problem56():
    maxsum = 0
    for a in range(100):
        for b in range(100):
            maxsum = max(maxsum,somme_chiffres10(a**b))
    print maxsum

problem56()
