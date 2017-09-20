#!/usr/bin/env python3

from collections import Counter

def sieve_list(N):
    P = [True]*N
    L = []
    for i in range(2,N):
        if P[i]:
            L.append(i)
            for k in range(2*i,N,i):
                P[k] = False
    return L

N = 1<<13  # elements in A are < 2^13, then so are their XORs
M = 10**9+7
P = sieve_list(N)

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        A = Counter(map(int,input().split()))  # O(n)
        # DP in O(K*N) where N = 2^13 (constant upper bound on XORs)
        # and K = len(A) is the number of distinct elements of A
        X = [0]*N
        X[0] = 1
        for a in A:
            nb_even = 1+A[a]//2     # picking an even (possibly 0) nb of a
            nb_odd = 1+(A[a]-1)//2  #            odd
            X1 = [(x*nb_even)%M for x in X]  # multisets with an even nb of a
            for x in range(N):               #                   odd
                X1[x] = (X1[x] + nb_odd*X[x^a]) % M
            X = X1
        # summing up prime XORs
        res = 0
        for x in P:
            res = (res + X[x]) % M
        print(res)

main()
