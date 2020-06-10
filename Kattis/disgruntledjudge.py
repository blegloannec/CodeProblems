#!/usr/bin/env python3

from math import gcd
import sys
input = sys.stdin.readline

MOD = 10001
F = lambda a,b: lambda x: (a*x + b) % MOD

def bezout(a, b):
    if b==0:
        return (a, 1, 0)
    g,u,v = bezout(b, a%b)
    return (g, v, u-(a//b)*v)

def inv_mod(a, n=MOD):
    g,u,_ = bezout(a, n)
    assert g==1
    return u

def solve_a(x1, x3, a):
    # x3 = a^2*x1 + (a+1)*b
    if gcd(a+1, MOD)==1:
        b = ((x3 - a*a*x1) * inv_mod(a+1)) % MOD
        yield b
    else:
        for b in range(MOD):
            if x3 == (a*a*x1 + (a+1)*b) % MOD:
                yield b

def solve(X):
    for a in range(MOD):
        for b in solve_a(X[0], X[1], a):
            Fab = F(a,b)
            if all(X[i]==Fab(Fab(X[i-1])) for i in range(2,len(X))):
                return (a,b)

def main():
    N = int(input())
    X = [int(input()) for _ in range(N)]
    a,b = solve(X)
    Fab = F(a,b)
    for x in X:
        sys.stdout.write(f'{Fab(x)}\n')

main()
