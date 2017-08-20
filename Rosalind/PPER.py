#!/usr/bin/env python3

M = 10**6

def fact(n):
    return 1 if n<=1 else (n*fact(n-1))%M

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

def pper(n,k):
    return (binom(n,k)*fact(k))%M

n,k = map(int,input().split())
print(pper(n,k))
