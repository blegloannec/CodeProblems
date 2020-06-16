#!/usr/bin/env python3

# C(n,k) = nb of colorings of a tree of size n with <=k colors
# There are k possible colors for the root, then, descending
# in the tree, for each node we can pick any of the k-1 colors
# not used for its parent.
# C(n,k) = k * (k-1)^(n-1)
# E(n,k) = nb of col. of a tree of size n with *exactly* k colors

P = 10**9+7

def inv_mod(n):
    return pow(n, P-2, P)

def C(n,k):
    return (k * pow(k-1, n-1, P)) % P

def count1(N, K):  # O(K^2 + K log N)
    # C(N,.) in O(K log N)
    E = [0,0] + [C(N,k) for k in range(2,K+1)]
    # E(N,.) in O(K^2) through DP:
    # E(N,k) = C(N,k) - ∑_{l<k} binom(k,l)*E(N,l)
    Binom = [1]*(K+1)
    for k in range(2,K+1):
        for l in range(k-1,0,-1):
            Binom[l] += Binom[l-1]
            Binom[l] %= P
        for l in range(2,k):
            E[k] -= Binom[l] * E[l]
            E[k] %= P
    return E[K]

def count2(N, K):  # O(K log N)
    # inclusion-exclusion
    # let us number the K colors and let
    # Xᵢ = set of colorings not using color i
    # |⋃ᵢ Xᵢ| = ∑ᵢ|Xᵢ| - ∑ᵢⱼ|Xᵢ∩Xⱼ| + ∑ᵢⱼₖ...
    #         = binom(K,1)*C(N,K-1) - binom(K,2)*C(N,K-2) + ...
    # E(N,K) = C(N,K) - |⋃ᵢ Xᵢ|
    E = 0
    Binom = 1
    for k in range(K):
        E += (-1 if k&1 else 1) * Binom * C(N, K-k)
        E %= P
        Binom *= (K-k) * inv_mod(k+1)
        Binom %= P
    return E

def main():
    N,K = map(int, input().split())
    print(count2(N,K))

main()
