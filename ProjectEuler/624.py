#!/usr/bin/env python3

# U(n) = nb de mots de taille n ne contenant pas le motif HH
#      = U(n-1) + U(n-2)
#      = Fibo(n+1)
# Pr[M=k] = U(k-3) / 2**k
#         = Fibo(k-2) / 2^k
# P(n) = Sum_{k=1..inf} Pr[M=kn]

# M = [ 0 1 ]
#     [ 1 1 ]
# P(n) = M^(-2) *  Sum_{k=1..inf} ( 1/2^n * M^n )^k

P = 10**9+9

def invmod(n):
    return pow(n,P-2,P)

class Matrix2:
    def __init__(self,a=1,b=0,c=0,d=1):
        self.m00,self.m01,self.m10,self.m11 = a,b,c,d
    
    def __add__(self,B):
        return Matrix2(self.m00+B.m00,self.m01+B.m01,self.m10+B.m10,self.m11+B.m11)
    
    def __neg__(self):
        return Matrix2(-self.m00,-self.m01,-self.m10,-self.m11)
    
    def __sub__(self,B):
        return self+(-B)
    
    def __mul__(self,B):
        return Matrix2((self.m00*B.m00+self.m01*B.m10)%P,(self.m00*B.m01+self.m01*B.m11)%P,(self.m10*B.m00+self.m11*B.m10)%P,(self.m10*B.m01+self.m11*B.m11)%P)
    
    def __pow__(self,n):
        if n==0:
            return Matrix2()
        if n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)
    
    def det(self):
        return (self.m00*self.m11-self.m01*self.m10)%P
    
    def inv(self):
        d = self.det()
        assert(d!=0)
        di = invmod(d)
        return Matrix2(self.m11*di,-self.m01*di,-self.m10*di,self.m00*di)

    def __str__(self):
        return '[[%d, %d], [%d, %d]]' % (self.m00,self.m01,self.m10,self.m11)

def QP(n):
    I = Matrix2()
    MFib = Matrix2(0,1,1,1)
    inv2 = invmod(2)
    R = Matrix2(0,inv2,inv2,inv2)**n
    S = (MFib**2).inv() * R*(I-R).inv()
    return S.m11

print(QP(10**18))
