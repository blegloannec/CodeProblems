#!/usr/bin/env python

from collections import defaultdict
from fractions import gcd
import random
random.seed()

# considerons un nb n = pi^ai (decomp primale) et le
# treillis oriente de ses diviseurs (qui sont de la
# forme pi^bi avec bi <= ai)
# il s'agit de compter le nombres de chemins de 1 a n
# la topologie de ce treillis ne depend que du
# multi-ensemble {{ai}}

# init avec i=0 et Y=[]
# mais attention, avec les appels nested a decr
# dans aux_count, on ne peut pas mettre Y=[] par defaut
# dans la definition (sinon le meme Y est re-utilise !)
def decr(X,i,Y):
    if i==len(X):
        Y = tuple(sorted(Y,reverse=True))
        if Y!=X:
            yield Y
    else:
        # cas x = 0 (on n'empile pas dans Y)
        for A in decr(X,i+1,Y):
            yield A
        # cas x > 0
        for x in xrange(1,X[i]+1):
            Y.append(x)
            for A in decr(X,i+1,Y):
                yield A
            Y.pop()

N = 10**16
            
# prog dyn pour le nb de gozinta pour le tuple d'exposants X
memo = {():1}
def count(X):
    if X in memo:
        return memo[X]
    res = 0
    for Y in decr(X,0,[]):
        res += count(Y)
        if res>N: # osef, on coupe, c'est perdu
            break
    memo[X] = res
    return res

# sous 10^16, on a au plus 13 facteurs premiers
P = [2,3,5,7,11,13,17,19,23,29,31,37,41]
# on genere les tuples possibles
def genX(i=0,X=[],n=1,A=53):
    if i<len(P):
        for a in xrange(1,A+1):
            n *= P[i]
            if n>N:
                break
            X.append(a)
            yield tuple(X)
            for Y in genX(i+1,X,n,a):
                yield Y
            X.pop()


def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
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

def miller_rabin(n,s=15):
    b = digits(n-1,2)
    for j in xrange(s):
        if witness(random.randint(1,n-1),n,b):
            return False
    return True

# Pollard's Rho
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
    while n%2==0:
        D[2] += 1
        n /= 2
    return factorisation(n,D)

def main():
    # verif pour 12 = 2^2.3, 48 = 2^4.3 et 120 = 2^3.3.5
    #print count((2,1)), count((4,1)), count((3,1,1))
    s = 1 # car g(1) = 1 !
    for X in genX():
        n = count(X)
        if n<=N:
            F = full_factorisation(n)
            Y = [F[i] for i in F]
            Y.sort(reverse=True)
            if X==tuple(Y):
                #print n
                s += n
    print s
    
main()
