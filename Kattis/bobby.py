#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def binom(n,k):
    return 1 if k==0 else n*binom(n-1,k-1)//k

def main():
    T = int(input())
    for _ in range(T):
        R,S,X,Y,W = map(int,input().split())
        WinConfs = sum(binom(Y,x) * (S-R+1)**x * (R-1)**(Y-x) for x in range(X,Y+1))
        print('yes' if W * WinConfs > S**Y else 'no')

main()
