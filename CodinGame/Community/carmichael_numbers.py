#!/usr/bin/env python3

def prim(n):
    if n%2==0:
        return False
    i = 3
    while i*i<=n:
        if n%i==0:
            return False
        i += 2
    return True

def carm(n):
    return all(pow(a,n,n)==a for a in range(1,n))

n = int(input())
print("YES" if not prim(n) and carm(n) else 'NO')
