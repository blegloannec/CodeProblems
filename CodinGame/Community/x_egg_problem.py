#!/usr/bin/env python3

# See ./two_egg_problem.py for the 2-egg version.
# Here, obviously, the min-max DP would not pass.

# For k eggs, a *k-strategy* is a sequence 0 < h0 < h1 < h2 < ... < n
# of floors to test with the first egg until it breaks.
# If the first egg breaks at h(i), then we switch to a (k-1)-strategy
# on the interval ]h(i-1),h(i)[.

# let O(k,n) = the minimal worst case complexity of a k-strategy for n floors
# let N(k,o) = the maximum n such that O(k,n) = o
# remember that N(2,o) = o(o+1)/2 = binom(o,2) + binom(o,1)
# and that we have O(k,n) = the minimum o such that N(k,o)>=n

# Assuming we know O(k,n), to build an optimal k-strategy, we choose
# h0 = N(k-1,O(k,n)-1), h1 = h0 + N(k-1,O(k,n)-2), h2 = h1 + N(k-1,O(k,n)-3), ...
# So that we have n <= sum_{0<=i<=O(k,n)-1} 1 + N(k-1,i)
# Assuming by induction that N(k-1,o) = sum_{1<=j<=k-1} binom(o,j)
# then n <= sum_{0<=o<=O(k,n)-1} 1 + sum_{1<=j<=k-1} binom(o,j)
# then n <= sum_{0<=o<=O(k,n)-1} sum_{0<=j<=k-1} binom(o,j)
#        <= sum_{0<=j<=k-1} sum_{0<=o<=O(k,n)-1} binom(o,j)
#        <= sum_{0<=j<=k-1} binom(O(k,n),j+1)  by Pascal's triangle column relation:
#                                              sum_{0<=i<=n) binom(i,k) = binom(n+1,k+1)
#        <= sum_{1<=j<=k} binom(O(k,n),j)
# hence N(k,o) = sum_{1<=j<=k} binom(o,j)


## DP (for checking purposes)
def dp(N,X):
    P = [[float('inf')]*(X+1) for _ in range(N+1)]
    for x in range(X+1):
        P[0][x] = 0
        P[1][x] = 1
    for n in range(N+1):
        P[n][1] = n
    for x in range(2,X+1):
        for n in range(2,N+1):
            for i in range(n+1):
                P[n][x] = min(P[n][x],1+max(P[i][x-1],P[n-i-1][x]))
    return P


## Formula
def binom(n,p):
    if not 0<=p<=n:
        return 0
    return 1 if p==0 else n*binom(n-1,p-1)//p

def formula(n,k):
    e = 1
    while sum(binom(e,i) for i in range(1,k+1))<n:
        e += 1
    return e

n = int(input())
x = int(input())
print(formula(n,x))
