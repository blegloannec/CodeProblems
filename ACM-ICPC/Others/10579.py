#!/usr/bin/env python3

import sys

class Matrix2:
    def __init__(self,a=1,b=0,c=0,d=1):
        self.m00,self.m01,self.m10,self.m11 = a,b,c,d
    def __mul__(self,B):
        return Matrix2(self.m00*B.m00+self.m01*B.m10,self.m00*B.m01+self.m01*B.m11,self.m10*B.m00+self.m11*B.m10,self.m10*B.m01+self.m11*B.m11)
    def __pow__(self,n):
        if n==0:
            return Matrix2()
        elif n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)

def main():
    F = Matrix2(0,1,1,1)
    for L in sys.stdin.readlines():
        M = F**(int(L)-1)
        print(M.m11)

main()
