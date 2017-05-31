#!/usr/bin/env python3

from math import log10

# exact same pb at HR

# somme geometrique rapide en O(log n) en exploitant le fait que :
# 1 + a + a^2 + ... + a^(2n+1) = (1 + a) * (1 + (a^2) + (a^2)^2 + ... + (a^2)^n)
# 1 + a + a^2 + ... + a^2n = 1 + a * (1 + a + a^2 + ... + a^(2*n-1))
#                          = 1 + a * (1 + a) * (1 + (a^2) + (a^2)^2 + ... + (a^2)^(n-1))

def geo_sum_mod(r,n,m):
    if n==0:
        return 1
    if n%2==1:
        return ((1+r)*geo_sum_mod((r*r)%m,(n-1)//2,m))%m
    return (1 + r*((1+r)*geo_sum_mod((r*r)%m,n//2-1,m))%m)%m

def main():
    T = int(input())
    for _ in range(T):
        A,N,M = map(int,input().split())
        if A==0:
            print(0)
        else:
            print((A*geo_sum_mod(pow(10,int(log10(A))+1,M),N-1,M))%M)

main()
