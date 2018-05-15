#!/usr/bin/env python

from collections import defaultdict
from math import sqrt,log
from fractions import gcd
import random
random.seed()


### FONCTIONS AUX
def digits2(n):
    c = []
    while n:
        c.append(n&1)
        n >>= 1
    return c

# Miller-Rabin
def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

# version deterministe 64 bits
def miller_rabin(n):
    b = digits2(n-1)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

# Pollard's rho
def pollard_rho(n):
    l = set()
    c = random.randint(1,n-1)
    f = (lambda x: (x*x+c)%n)
    x = random.randint(0,n-1)
    y = x
    x = f(x)
    y = f(f(y))
    while x!=y:
        p = gcd(n,abs(x-y))
        if 1<p<n:
            return p
        x = f(x)
        y = f(f(y))
    return None

def factorisation(n,D):
    while n>1:
        if miller_rabin(n):
            D[n] += 1
            return D
        f = pollard_rho(n)
        if f!=None:
            factorisation(f,D)
            n /= f
    return D

def full_factorisation(n):
    D = defaultdict(int)
    while n&1==0:
        D[2] += 1
        n >>= 1
    return factorisation(n,D)

def eulerphi(n):
    res = 1
    F = full_factorisation(n)
    for p in F:
        m = F[p]
        res *= (p-1)*p**(m-1)
    return res

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    #assert(gcd(p,q)==1)
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def rev_chinois_list(E):
    x,y = 0,1
    for a,p in E:
        x = rev_chinois(x,y,a,p)
        y *= p
    return x
### FIN AUX


# version non modulaire
def hypexp(a,k):
    if k==0:
        return 1
    return pow(a,hypexp(a,k-1))

# comparateur hypexp(a,k) >= x
def hypexpbigger(a,k,x):
    if k==0:
        return 1>=x
    elif a>=x:
        return True
    else:
        # a^h >= x, h >= log_a(x)
        return hypexpbigger(a,k-1,log(x,a))

# Th d'Euler : si a et n pee alors a^phi(n) = 1 mod n    
def hypexpmod(a,k,m):
    if k==0:
        return 1
    elif m==1:
        return 0
    elif gcd(a,m)==1:
        return pow(a,hypexpmod(a,k-1,eulerphi(m)),m)
    else:
        # cas difficile, on decompose m et on traite chaque facteur premier
        # separement, on recompose par theoreme chinois
        D = full_factorisation(m)
        E = []
        for p in D:
            q = p**D[p]
            if a%p!=0:
                phiq = (p-1)*p**(D[p]-1)
                E.append((pow(a,hypexpmod(a,k-1,phiq),q),q))
            else:
                x = a/p
                y = 1
                while x%p==0:
                    x /= p
                    y += 1
                # p^y | a
                if hypexpbigger(a,k-1,float(D[p])/y):
                    # q | hypexp(a,k)
                    E.append((0,q))
                else:
                    E.append((pow(a,hypexp(a,k-1),q),q))
        return rev_chinois_list(E)

def main():
    Q = int(input())
    for _ in xrange(Q):
        a,b,m = map(int,raw_input().split())
        print hypexpmod(a,b,m)

main()
