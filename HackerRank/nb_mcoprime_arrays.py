#!/usr/bin/env python

import sys
from math import sqrt

# on ajoute iterativement les facteurs premiers pi^ai de m
# si l'on connait le nb de m-tableaux de taille n de m
# calculons le nb de m'-tableaux pour m' = m * pi^ai
# pour en fabriquer, on prend un m-tableau dans lequel on
# selectionne un sous-ensemble de cases jamais consecutives
# pour recevoir des p^b avec 1<=b<=a+i
# le nb de telles selections verifie Si(n) = Si(n-1) + ai*Si(n-2)
# (donc on peut calculer ce nb par exponentiation d'une matrice 2x2)
# et il suffit de multiplier le nb courant de m-tableaux par Si(n)
# pour obtenir le nb de m'-tableaux

def sieve(N):
    P = [True]*N
    P[0] = P[1] = False
    L = []
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                if P[k]:
                    P[k] = False
    return P,L

N = 10**6
Pr,LPr = sieve(N)

def digits2(n):
    c = []
    while n>0:
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
    if n<N:
        return Pr[n]
    b = digits2(n-1)
    for w in [2,325,9375,28178,450775,9780504,1795265022]:
        if witness(w,n,b):
            return False
    return True

P = 10**9+7

class Matrix2:
    def __init__(self,a=1,b=0,c=0,d=1):
        self.m00,self.m01,self.m10,self.m11 = a,b,c,d
    def __mul__(self,B):
        return Matrix2((self.m00*B.m00+self.m01*B.m10)%P,(self.m00*B.m01+self.m01*B.m11)%P,(self.m10*B.m00+self.m11*B.m10)%P,(self.m10*B.m01+self.m11*B.m11)%P)
    def __pow__(self,n):
        if n==0:
            return Matrix2()
        if n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)
    
def coeff(a,n):
    M = Matrix2(1,a,1,0)**(n-1)
    return ((a+1)*M.m00+M.m01)%P

# MAIN
def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        n,m = map(int,sys.stdin.readline().split())
        D = []
        for p in LPr:
            if m%p==0:
                c = 1
                m /= p
                while m%p==0:
                    m /= p
                    c += 1
                D.append(c)
        if m>1:
            if miller_rabin(m):
                D.append(1)
            else:
                s = int(sqrt(m))
                if s*s==m:
                    D.append(2)
                else:
                    D.append(1)
                    D.append(1)
        res = 1
        for d in D:
            res = (res*coeff(d,n))%P
        print res

main()
