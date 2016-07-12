#!/usr/bin/env python3

from decimal import *
getcontext().prec = 20

D2 = Decimal(2)
Dp = Decimal('30.403243784')
Dm = Decimal(10**(-9))
def f(x):
    return int(D2**(Dp-x*x))*Dm;

def floyd(f,u0):
    x = f(u0)
    y = f(x)
    while x!=y:
        x = f(x)
        y = f(f(x))
    l0 = 0
    x = u0
    while x!=y:
        x = f(x)
        y = f(y)
        l0 += 1
    l1 = 1
    y = f(y)
    while x!=y:
        y = f(y)
        l1 += 1
    return l0,l1

def main():
    l0,l1 = floyd(f,Decimal(-1))
    # 516, 2
    u = Decimal(-1)
    for _ in range(l0):
        u = f(u)
    print(u+f(u))

main()
