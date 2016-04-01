#!/usr/bin/env python

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def somme_chiffres10(n):
    return sum(chiffres10(n))

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def problem20():
    print somme_chiffres10(fact(100))

problem20()
