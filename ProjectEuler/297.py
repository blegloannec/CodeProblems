#!/usr/bin/env python

from bisect import *

def fibo(M):
    u0,u1 = 1,2
    U = [1]
    while u1<M:
        U.append(u1)
        u1,u0 = u1+u0,u1
    return U

L = fibo(10**17)

# greedy zeck decomp (not used)
def zeck(n):
    i = len(L)-1
    D = []
    while n>0:
        if L[i]<=n:
            D.append(L[i])
            n -= L[i]
        i -= 1
    return D

## Formule recursive pour la somme des nb de termes
# sumzeck(n) = sommes des nb de termes de [0,n]
# si F est le plus grand terme de la suite de Fibo
# dans [0,n], alors la somme pour les termes [0,F-1]
# est sumzeck(F-1), et les (n-F+1) termes de l'intervalle
# [F,n] utilisent F dans leur decomposition, apres quoi ils
# deviennent [0,n-F] dont la somme est sumzeck(n-F)
memo = {0:0,1:1}
def sumzeck(n):
    if n in memo:
        return memo[n]
    i = bisect_right(L,n)-1
    res = sumzeck(L[i]-1)+sumzeck(n-L[i])+(n-L[i]+1)
    memo[n] = res
    return res

#print sumzeck(10**6-1)
print sumzeck(10**17-1)
