#!/usr/bin/env python3

# Seeing F(n) as a matrix exponentiation M^n, the sum looks much more manageable.
# A tricky insight about F allows us to deal with the absolute value for free (cf. below).

P = 10**9+7

def inv_mod(n):
    return pow(n, P-2, P)

class Matrix2:
    def __init__(self, a=1, b=0, c=0, d=1):
        self.m00, self.m01, self.m10, self.m11 = a%P, b%P, c%P, d%P
    
    def __add__(self, B):
        return Matrix2(self.m00+B.m00, self.m01+B.m01, self.m10+B.m10, self.m11+B.m11)
    
    def __mul__(self, B):
        return Matrix2(self.m00*B.m00+self.m01*B.m10, self.m00*B.m01+self.m01*B.m11, \
                       self.m10*B.m00+self.m11*B.m10, self.m10*B.m01+self.m11*B.m11)
    
    def __pow__(self, n):
        if n==0:
            return Matrix2()
        if n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)
    
    def det(self):
        return (self.m00*self.m11 - self.m10*self.m01) % P
    
    def inverse(self):
        det = self.det()
        assert det!=0
        inv_det = inv_mod(det)
        return Matrix2(self.m11*inv_det, -self.m01*inv_det, \
                       -self.m10*inv_det, self.m00*inv_det)
    
    def eval(self, u0=1, u1=3):  # init. values
        return (self.m00*u0 + self.m01*u1) % P


def main():
    F = Matrix2(0,1,-1,6)
    Finv = F.inverse()
    # Finv is the matrix of the reverse relation:
    #   F(n+2) = 6F(n+1) - F(n)  <==>  F(n) = 6F(n+1) - F(n+2)
    # which is actually the same (because of this -1 coeff.)!
    # (Finv is simply F with all lines and colums reversed.)
    # And as "F(-1)" = 3 = F(1), then obviously "F(-n)" = F(n) for all n.
    # This allows us to deal with the absolute value in F for free!
    N = int(input())
    A = list(map(int,input().split()))
    S = Matrix2()
    for a in A:
        S *= F**a + Finv**a
    print(S.eval())

main()
