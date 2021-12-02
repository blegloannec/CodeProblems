#!/usr/bin/env python3

def simu(P,i):
    for c,x in P:
        if c=='&':
            i &= x
        elif c=='|':
            i |= x
        else:
            i ^= x
    return i

def simpl(P):
    out0,out1 = simu(P,0),simu(P,1023)
    A,O,X = 1023,0,0
    for i in range(10):
        B01 = (out0>>i)&1,(out1>>i)&1
        if B01==(0,0):
            A ^= 1<<i
        elif B01==(1,0):
            X |= 1<<i
        elif B01==(1,1):
            O |= 1<<i
    return A,O,X

def main():
    n = int(input())
    P = []
    for _ in range(n):
        c,x = input().split()
        P.append((c,int(x)))
    A,O,X = simpl(P)
    print(3)
    print('&',A)
    print('|',O)
    print('^',X)

main()
