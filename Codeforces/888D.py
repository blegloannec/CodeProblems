#!/usr/bin/env python3

# soit S(n,k) = nb de permutations sur n avec k points-fixes
# S(n,k) = binom(n,k) * S(n-k,0)
# https://oeis.org/A000166
S0 = [1,0,1,2,9]

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

n,k = map(int,input().split())
res = sum(binom(n,i)*S0[i] for i in range(k+1))
print(res)
