#!/usr/bin/env python3

# had to use pypy3 to pass!...

class ComplexMod:
    def __init__(self, a, b, m):
        self.a = a % m
        self.b = b % m
        self.m = m
    
    def __mul__(self, C):
        assert(self.m==C.m)
        x = (self.a*C.a)%self.m - (self.b*C.b)%self.m
        y = (self.a*C.b)%self.m + (self.b*C.a)%self.m
        return ComplexMod(x,y,self.m)
    
    def __pow__(self, k):
        #assert(k>=0)
        if k==0:
            return ComplexMod(1,0,self.m)
        if k&1==0:
            return (self*self)**(k>>1)
        return self*(self*self)**(k>>1)


def main():
    T = int(input())
    for _ in range(T):
        a,b,k,m = map(int,input().split())
        x = ComplexMod(a,b,m)**k
        print(x.a,x.b)

main()
