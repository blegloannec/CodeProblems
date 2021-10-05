#!/usr/bin/env python3

class Die:
    #  c
    # eabd
    #  f
    def __init__(self):
        self.c = int(input()[1])
        self.e,self.a,self.b,self.d = map(int, input())
        self.f = int(input()[1])

    def standard(self):
        return self.a+self.d==self.b+self.e==self.c+self.f==7

    def hturn(self, it=1):
        for _ in range(it%4):
            self.e,self.a,self.b,self.d = self.a,self.b,self.d,self.e

    def vturn(self, it=1):
        for _ in range(it%4):
            self.c,self.a,self.f,self.d = self.d,self.c,self.a,self.f

    def rot(self, it=1):
        for _ in range(it%4):
            self.b,self.c,self.e,self.f = self.f,self.b,self.c,self.e

    def __str__(self):
        return f' {self.c}\n{self.e}{self.a}{self.b}{self.d}\n {self.f}'

    def normalize(self):
        if self.c==1:
            self.vturn()
        elif self.f==1:
            self.vturn(-1)
        while self.a!=1:
            self.hturn()
        assert self.d!=2
        while self.b!=2:
            self.rot()

def main():
    D = Die()
    if D.standard():
        D.normalize()
        print('right-handed' if D.c==3 else 'left-handed')
    else:
        print('degenerate')

main()
