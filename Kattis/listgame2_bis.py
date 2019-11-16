#!/usr/bin/env python3

from functools import lru_cache
from collections import defaultdict
from math import gcd
import random
random.seed()

@lru_cache(maxsize=None)
def game(n,i):
    res = 1
    for j in range(i,len(Div)):
        d = Div[j]
        if d*d>n:
            break
        q,r = divmod(n,d)
        if r==0 and Div[j+1]<=q:
            b = 1 + game(q, j+1)
            if b<res:
                break
            else:
                res = b
    return res


# Miller-Rabin
def witness(a,n,b):
    d = 1
    for i in range(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n):
    if n<2:
        return False
    m = n-1
    b = []
    while m:
        b.append(m&1)
        m >>= 1
    for w in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if w%n!=0 and witness(w,n,b):
            return False
    return True

def pollard_rho(n):
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
            n //= f
    return D

def full_factorisation(n):
    D = defaultdict(int)
    while n&1==0:
        D[2] += 1
        n >>= 1
    return factorisation(n,D)


def main():
    global Div
    N = int(input())
    D = full_factorisation(N)
    Div = [1]
    for p,m in D.items():
        q = p
        L = len(Div)
        for _ in range(m):
            for i in range(L):
                Div.append(q*Div[i])
            q *= p
    Div.sort()
    print(game(N,1))

main()
