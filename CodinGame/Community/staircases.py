#!/usr/bin/env python3

# Denombrement assez classique analogue aux partitions d'entiers.
# En l'occurrence, il s'agit du nb de partitions en au moins 2 composantes
# distinctes (http://oeis.org/A111133).

memo = {}
def S(n,k):
    k = min(n,k)
    if n==0:
        return 1
    if k==0:
        return 0
    if (n,k) in memo:
        return memo[n,k]
    res = S(n,k-1)
    if n>=k:
        res += S(n-k,k-1)
    memo[n,k] = res
    return res

n = int(input())
print(S(n,n-1))
