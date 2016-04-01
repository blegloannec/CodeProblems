#!/usr/bin/env python

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def somme_chiffres10(n):
    return sum(chiffres10(n))

def problem16():
    print somme_chiffres10(2**1000)

problem16()
