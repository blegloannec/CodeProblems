#!/usr/bin/env python3

class Die:
    #  c
    # eabd
    #  f
    def __init__(self):
        self.c = int(input()[1])
        self.e,self.a,self.b,self.d = map(int, input())
        self.f = int(input()[1])

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

def main():
    D = Die()
    Com = input()
    for c in Com:
        if c=='D':
            D.rot(2)
        elif c=='R':
            D.rot()
        elif c=='L':
            D.rot(-1)
        D.vturn()
    print(D.a)

main()
