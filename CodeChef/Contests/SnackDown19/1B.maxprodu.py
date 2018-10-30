#!/usr/bin/env python3

# comme (x^2-x) = x(x-1) le pb est equivalent a maximiser
# Prod_i x_i  et  Prod_i (x_i-1)  simultanement
# ce qui est obtenu dans le continu en ayant x_i ~ N/K
# si N < K(K+1)/2 = 1+...+K il n'y a pas de solution
# si N = K(K+2)/2, la seule decomposition (1,2,...,K)
# et pour les N suivants le meilleur equilibre est obtenu en
# incrementant les composantes une a une de la derniere a la premiere,
# puis l'on recommence...
# N = K(K+1)/2,     (1, 2, ..., K-1, K)
# N = K(K+1)/2+1,                   +1
# N = K(K+1)/2+2,              +1
#                        ...
# N = K(K+1)/2+K,   +1
# N = K(K+1)/2+K+1,                 +1
# N = K(K+1)/2+K+2,            +1
# chaque cas est donc traite en O(K)

P = 10**9+7

def maxprod(N,K):
    M = K*(K+1)//2
    if N<M:
        return -1
    prod = 1
    for i in range(K):
        x = (N-M+i)//K+1+i
        x = (x*(x-1)) % P
        prod = (prod*x) % P
    return prod

def main():
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        print(maxprod(N,K))

main()
