#!/usr/bin/env python3

# recycled from CG/x_egg_problem.py

from functools import lru_cache
import sys
input = sys.stdin.readline

@lru_cache(maxsize=None)
def binom(n, p):
    if not 0<=p<=n:
        return 0
    return 1 if p==0 else n*binom(n-1, p-1)//p

@lru_cache(maxsize=None)
def sum_binom(e, x):
    #return sum(binom(e,i) for i in range(1,x+1))
    return 0 if x==0 else sum_binom(e, x-1) + binom(e, x)

def formula(n, x):
    e = 1
    while e<33 and sum_binom(e, x)<n:
        e += 1
    return e

def main():
    T = int(input())
    for _ in range(T):
        n,x = map(int, input().split())
        res = formula(n,x)
        if res<=32:
            sys.stdout.write(f'{res}\n')
        else:
            sys.stdout.write('Impossible\n')

main()
