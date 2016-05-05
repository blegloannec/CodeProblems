#!/usr/bin/env python

from fractions import gcd,Fraction
from math import *

#sys.setrecursionlimit(100000)

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

def lcm(a,b):
    return a*b/gcd(a,b)

def somme_diviseurs(n): # for n>1!
    s = 1
    r = int(sqrt(n))
    if r*r==n: # n is a square
        s += r
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += i+n/i
    return s

def nb_diviseurs(n): # for n>1!
    s = 2
    r = int(sqrt(n))
    if r*r==n: # n is a square
        s += 1
        r -= 1
    for i in xrange(2,r+1):
        if n%i==0:
            s += 2
    return s

def sieve_nb_divisors(N):
    P = [True for _ in xrange(N)]
    Nbdiv = [1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Nbdiv[i] = 2
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                j = 1
                while l%i==0:
                    l /= i
                    j += 1
                Nbdiv[k] *= j+1
    return P,Nbdiv

def prime(n):
    if n%2==0:
        return False
    for i in xrange(3,int(sqrt(n))+1,2):
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

def mirror(n):
    m = 0
    while n>0:
        m = 10*m + n%10
        n /= 10
    return m

def is_palindrome(n):
    return mirror(n)==n

def taux_lettres(m):
    cpt = 0
    for c in m:
        if (ord('a')<=c and c<=ord('z')) or (ord('A')<=c and c<=ord('Z')):
            cpt += 1
    return float(cpt)/len(m)

def indice_coincidence(m):
    cpt = [0 for _ in xrange(26)]
    N = 0
    for c in m:
        if ord('a')<=c and c<=ord('z'):
            cpt[c-ord('a')] += 1
            N += 1
        elif ord('A')<=c and c<=ord('Z'):
            cpt[c-ord('A')] += 1
            N += 1
    return float(sum(map((lambda(x):x*(x-1)),cpt)))/(N*(N-1))

def digits(n,b):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def digits_sum(n,b):
    return sum(digits(n,b))

def nb_digits10(n):
    return int(log10(n))+1

# t = n(n+1)/2
# n^2 + n - 2t = 0
# Given t, D = 1+8t must be a square
# then n = (-1+sqrt(D))/2

def is_triang(t):
    D = 1+8*t
    d = int(sqrt(1+8*t))
    return d*d==D

# p = n(3n-1)/2
# 3n^2 - n - 2p = 0
# D = 1+24p
# et n = (1+sqrt(D))/6
# mais les solutions pour n<0 ont n = (1-sqrt(D))/6
# dans ce cas (1-sqrt(D))%6 == 0
# donc (1+sqrt(D))%6 == 2 != 0

def is_penta(p):
    D = 1+24*p
    d = int(sqrt(D))
    return (d*d==D and (1+d)%6==0)


# Miller-Rabin
def witness(a,n):
    b = digits(n-1,2)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

# permutation suivante (ordre lex) d'un tableau quelconque
# (repetitions autorisees)
# (pour prev_permutation, inverser les comparaisons de T[.])
def next_permutation(T):
    pivot = len(T)-2
    while pivot>=0 and T[pivot]>=T[pivot+1]:
        pivot -= 1
    if pivot<0:
        return False
    swap = len(T)-1
    while T[swap]<=T[pivot]:
        swap -= 1
    T[swap],T[pivot] = T[pivot],T[swap]
    i = pivot+1
    j = len(T)-1
    while i<j:
        T[i],T[j] = T[j],T[i]
        i += 1
        j -= 1
    return True
