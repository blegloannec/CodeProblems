#!/usr/bin/env python3

class Poly:
    def __init__(self,C=None):
        if C is None:
            C = []
        elif isinstance(C,str):
            self.C = []
            self.parse(C)
        else:
            self.C = C
        self.reduce()

    def parse(self, S):
        S = S.replace('-','+-').split('+')
        for M in S:
            M = M.split('x')
            if len(M)==1:
                self[0] = int(M[0])
            else:
                A,B = M
                d = int(B[1:]) if B else 1
                self[d] = -1 if A=='-' else int(A) if A else 1

    def deg(self):  # -1 pour le polynome 0
        return len(self.C)-1

    def is_zero(self):
        return self.deg()<0
    
    def reduce(self):
        while self.deg()>=0 and self[-1]==0:
            self.C.pop()

    def __getitem__(self,i):
        return self.C[i] if i<=self.deg() else 0

    def __setitem__(self,i,x):
        while self.deg()<i:
            self.C.append(0)
        self.C[i] = x
        self.reduce()
    
    def __add__(self,Q):
        d = max(self.deg(),Q.deg())
        R = [0]*(d+1)
        for i in range(d+1):
            R[i] = self[i]+Q[i]
        return Poly(R)

    def __sub__(self,Q):
        d = max(self.deg(),Q.deg())
        R = [0]*(d+1)
        for i in range(d+1):
            R[i] = self[i]-Q[i]
        return Poly(R)
    
    def __mul__(self,Q):
        d = self.deg()+Q.deg()
        R = [0]*(d+1)
        for a in range(self.deg()+1):
            for b in range(Q.deg()+1):
                R[a+b] += self[a]*Q[b]
        return Poly(R)

    def __neg__(self):
        return Poly([-c for c in self.C])

    def __pow__(self,n):
        if n==0:
            return Poly([1])
        if n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)
    
    def copy(self):
        return Poly(self.C[:])

    def str_mono(self,i):
        assert(i<=self.deg())
        c = self[i]
        if c==0:
            return ''
        sgn = '-' if c<0 else '' if i==self.deg() else '+'
        c = abs(c)
        pref = str(c) if c!=1 or i==0 else ''
        suff = 'x^%d'%i if i>1 else 'x' if i==1 else ''
        return sgn+pref+suff
    
    def __str__(self):
        if self.is_zero():
            return '0'
        return ''.join(self.str_mono(i) for i in range(self.deg(),-1,-1) if self[i]!=0)


poly = input().replace(')(',')*(').replace(')^',')**').replace('(','Poly("').replace(')','")')
print(eval(poly))
