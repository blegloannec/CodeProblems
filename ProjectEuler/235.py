#!/usr/bin/env python

from decimal import Decimal

def u(r,k):
    return (900-3*k)*r**(k-1)

# formule de la somme
def s(r,n):
    return 900*(1-r**n)/(1-r) - 3*(1+(r-r**n)/(1-r)-n*r**n)/(1-r)

# derivee (merci wolfram alpha ;) )
def ds(r,n):
    return -(3*n**2*r**(n-1))/(r-1)+n*((3*(r+1))/(r-1)**2+900/(r-1))*r**(n-1)-(6*(150*r-149)*(r**n-1))/(r-1)**3

def f(x):
    return s(x,5000)+6*10**11

def df(x):
    return ds(x,5000)

# methode de newton
def newton(f,df,x0,n):
    for _ in xrange(n):
        x0 -= f(x0)/df(x0)
    return x0

print newton(f,df,Decimal(1.1),500)
# arrondi a 12 decimales : 1.002322108633
