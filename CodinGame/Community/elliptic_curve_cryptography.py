#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Elliptic_curve#The_group_law

import copy

P = 0x3fddbf07bb3bc551  # prime
Gx = 0x69d463ce83b758e
Gy = 0x287a120903f7ef5c
assert (Gy**2 - Gx**3 - 7)%P==0

def invmod(x):
    return pow(x,P-2,P)

class Point:
    def __init__(self, x=None, y=None):
        if y is None:
            self.neutral = True
        else:
            self.neutral = False
            self.x = x % P
            self.y = y % P

    def copy(self):
        return copy.copy(self)

    def __add__(self, B):
        if self.neutral:
            return B.copy()
        if B.neutral:
            return self.copy()
        if self.x==B.x:
            if (self.y+B.y)%P==0:
                return Point()
            else:
                L = ((3*self.x*self.x)*invmod(2*self.y)) % P
        else:
            L = ((B.y-self.y)*invmod(B.x-self.x)) % P
        X = (L*L - self.x - B.x) % P
        Y = (L*(self.x - X) - self.y) % P
        return Point(X,Y)

    def __rmul__(self, k):
        assert isinstance(k,int) and k>=0
        if k==0:
            return Point()
        res = (k//2)*(self+self)
        if k&1:
            res += self
        return res


if __name__=='__main__':
    G = Point(Gx,Gy)
    N = int(input())
    for _ in range(N):
        K = int(input()[2:],16)
        print(hex((K*G).x))
