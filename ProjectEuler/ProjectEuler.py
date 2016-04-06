#!/usr/bin/python

from fractions import gcd,Fraction
from math import *

#sys.setrecursionlimit(100000)

## Fonctions auxiliaires
def lcm(a,b):
    return a*b/gcd(a,b)

def somme_diviseurs(n):
    s = 1
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            s += i+n/i
    return s

def nb_diviseurs(n):
    s = 2
    r = int(sqrt(n))
    if n%r==0:
        s += 1
    for i in range(2,r):
        if n%i==0:
            s += 2
    return s

def premier(n):
    if n<0 or n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def miroir(n):
    m = 0
    while n!=0:
        m = 10*m + n%10
        n /= 10
    return m

def palindrome(n):
    return miroir(n)==n

def taux_lettres(m):
    cpt = 0
    for c in m:
        if (ord('a')<=c and c<=ord('z')) or (ord('A')<=c and c<=ord('Z')):
            cpt += 1
    return float(cpt)/len(m)

def indice_coincidence(m):
    cpt = [0 for i in range(26)]
    N = 0
    for c in m:
        if ord('a')<=c and c<=ord('z'):
            cpt[c-ord('a')] += 1
            N += 1
        elif ord('A')<=c and c<=ord('Z'):
            cpt[c-ord('A')] += 1
            N += 1
    return float(sum(map((lambda(x):x*(x-1)),cpt)))/(N*(N-1))

def chiffres10(n):
    c = []
    while n>0:
        c.append(n%10)
        n /= 10
    return c

def somme_chiffres10(n):
    return sum(chiffres10(n))
