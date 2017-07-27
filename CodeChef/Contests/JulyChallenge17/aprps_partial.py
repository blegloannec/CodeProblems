#!/usr/bin/env python

from math import sqrt
#from fractions import *

def size(M):
    return len(M),len(M[0])

def id(n):
    return [[int(i==j) for j in xrange(n)] for i in xrange(n)]

def copy(M):
    h,_ = size(M)
    return [M[i][:] for i in xrange(h)]

def l_swap(M,i,j):
    w = len(M[0])
    for k in xrange(w):
        M[i][k],M[j][k] = M[j][k],M[i][k]

def first_non_zero(M,i):
    h = len(M)
    for j in xrange(i,h):
        if M[i][j]!=0:
            return j
    return None

def sline_prod(a,M,i):
    w = len(M[0])
    for j in xrange(w):
        M[i][j] *= a

def line_diff(a,M,i,j):
    # Mj <- Mj - a*Mi
    w = len(M[0])
    for k in xrange(w):
        M[j][k] -= a*M[i][k]

def det(M0):
    d = 1
    M = copy(M0)
    n = len(M)
    for i in xrange(n):
        j0 = first_non_zero(M,i)
        if j0==None:
            return 0
        if j0>i:
            l_swap(M,i,j0)
            d = -d
        a = Fraction(1,M[i][i]) # for exact Fraction computation
        d *= M[i][i]
        sline_prod(a,M,i)
        for j in xrange(n):
            if j!=i:
                a = M[j][i]
                line_diff(a,M,i,j)
    return d


MOD = 10**9+7

def inv_mod(x):
    return pow(x,MOD-2,MOD)

class Poly:
    def __init__(self,C=None):
        if C==None or len(C)==0:
            C = [0]
        self.C = C  #map(Fraction,C)  # add [:] for copy
        self.reduce()

    def deg(self):
        return len(self.C)-1

    def is_zero(self):
        return self.deg()==0 and self[0]==0
    
    def reduce(self):
        while self.deg()>0 and self[-1]==0:
            self.C.pop()

    def __getitem__(self,i):
        return self.C[i] if i<=self.deg() else 0

    def __setitem__(self,i,x):
        while self.deg()<=i:
            self.C.append(0)
        self.C[i] = x%MOD
    
    def __add__(self,Q):
        d = max(self.deg(),Q.deg())
        R = [0]*(d+1)
        for i in xrange(d+1):
            R[i] = (self[i]+Q[i]) % MOD
        return Poly(R)

    def __sub__(self,Q):
        d = max(self.deg(),Q.deg())
        R = [0]*(d+1)
        for i in xrange(d+1):
            R[i] = (self[i]-Q[i]) % MOD
        return Poly(R)
    
    def __mul__(self,Q):
        d = self.deg()+Q.deg()
        R = [0]*(d+1)
        for a in xrange(self.deg()+1):
            for b in xrange(Q.deg()+1):
                R[a+b] = (R[a+b] + self[a]*Q[b]) % MOD
        return Poly(R)

    def __neg__(self):
        return Poly([(-c)%MOD for c in self.C])
    
    def copy(self):
        return Poly(self.C[:])

    #def shift(self,i):
    #    return Poly([0]*i + self.C)
    
    def divmod(self,B):
        assert(not B.is_zero())
        R = self.copy()
        Q = Poly()
        while not R.is_zero() and R.deg()>=B.deg():
            #X = Poly([Fraction(R[-1],B[-1])]).shift(R.deg()-B.deg())
            x = (R[-1]*inv_mod(B[-1]))%MOD
            Q[R.deg()-B.deg()] = x
            for i in xrange(B.deg()+1):
                R[R.deg()-B.deg()+i] -= (x*B[i])%MOD
            R.reduce()
        Q.reduce()
        return (Q,R)

    def __div__(self,B):
        return self.divmod(B)[0]

    def __mod__(self,B):
        return self.divmod(B)[1]

    @staticmethod
    def gcd(A,B):
        while not B.is_zero():
            A,B = B,A%B
        return A  #.copy()
    
    def str_mono(self,i):
        assert(i<=self.deg())
        pref = str(self[i]) if self[i]!=1 or i==0 else ''
        suff = 'X^'+str(i) if i>1 else 'X' if i==1 else ''
        return pref+suff
    
    def __str__(self):
        if self.is_zero():
            return '0'
        return ' + '.join(self.str_mono(i) for i in xrange(self.deg(),-1,-1) if self[i]!=0)

class RationalFraction:
    def __init__(self,P,Q):
        assert(not Q.is_zero())
        self.P = P
        self.Q = Q
        self.reduce()

    def is_zero(self):
        return self.P.is_zero()

    def reduce(self):
        G = Poly.gcd(self.P,self.Q)
        self.P /= G
        self.Q /= G

    @staticmethod
    def unit():
        return RationalFraction(Poly([1]),Poly([1]))
        
    def __mul__(self,B):
        return RationalFraction(self.P*B.P,self.Q*B.Q)

    def __div__(self,B):
        return RationalFraction(self.P*B.Q,self.Q*B.P)
        
    def __add__(self,B):
        return RationalFraction(self.P*B.Q+B.P*self.Q,self.Q*B.Q)

    def __sub__(self,B):
        return RationalFraction(self.P*B.Q-B.P*self.Q,self.Q*B.Q)

    def __neg__(self):
        return RationalFraction(-self.P,self.Q)
    
    def inv(self):
        return RationalFraction(self.Q,self.P)
    
    def __str__(self):
        return '%s // %s' % (str(self.P),str(self.Q))


def fraction_first_non_zero(M,i):
    h = len(M)
    for j in xrange(i,h):
        if not M[i][j].is_zero():
            return j
    return None

def polydet(M0):
    d = RationalFraction.unit()
    M = copy(M0)
    n = len(M)
    for i in xrange(n):
        j0 = fraction_first_non_zero(M,i)
        if j0==None:
            return 0
        if j0>i:
            l_swap(M,i,j0)
            d = -d
        a = M[i][i].inv()
        d *= M[i][i]
        d.reduce()
        sline_prod(a,M,i)
        for j in xrange(n):
            if j!=i:
                a = M[j][i]
                line_diff(a,M,i,j)
    #d.reduce()
    return d

#https://en.wikipedia.org/wiki/Resultant#Number_theory

def fractionize(M):
    for i in xrange(len(M)):
        for j in xrange(len(M)):
            M[i][j] = RationalFraction(M[i][j],Poly([1]))

def res_const(P,a):
    PC = [Poly([x]) for x in P.C]
    M = []
    Qdeg = 2
    QC = [Poly([-a,0,1]),Poly([0,-2]),Poly([1])]
    n = P.deg()+Qdeg
    for i in xrange(Qdeg):
        M.append([Poly() for _ in xrange(i)] + PC[::-1] + [Poly() for _ in xrange(n-1-i-P.deg())])
    for i in xrange(P.deg()):
        M.append([Poly() for _ in xrange(i)] + QC[::-1] + [Poly() for _ in xrange(n-1-i-Qdeg)])
    fractionize(M)
    R = polydet(M)
    assert(R.Q.deg()==0)
    return R.P

def is_sqr(x):
    return int(sqrt(x))**2==x

def main():
    T = int(raw_input())
    for _ in range(T):
        n = int(raw_input())
        A = map(int,raw_input().split())
        S = filter(is_sqr,A)
        P = Poly([-sum(int(sqrt(s)) for s in S),1]) if S else None
        for a in A:
            if not is_sqr(a):
                if P==None:
                    P = Poly([-a,0,1])
                else:
                    P = res_const(P,a)
            #print P
        print P.deg()
        print ' '.join(str(P[i]%MOD) for i in xrange(P.deg()+1))

main()
