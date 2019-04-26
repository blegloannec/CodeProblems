#!/usr/bin/env python3

from itertools import combinations_with_replacement as Combi
from collections import defaultdict

def main0():  # pythonic variant
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        S = list(map(int,input().split()))
        A = [S[0]//K]
        PendingSums = defaultdict(int)
        i = 1
        for _ in range(N-1):
            while S[i] in PendingSums:
                if PendingSums[S[i]]==1:
                    del PendingSums[S[i]]
                else:
                    PendingSums[S[i]] -= 1
                i += 1
            a = S[i] - (K-1)*A[0]
            # using itertools to compute the new sums to consider
            # (not optimal because of the repeated calls to sum(C))
            for k in range(K):
                for C in Combi(A,k):
                    s = sum(C) + (K-k)*a
                    PendingSums[s] += 1
            A.append(a)
        print(*A)

def main1():  # more academic variant
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        S = list(map(int,input().split()))
        A = [S[0]//K]
        Sums = [[k*A[0]] for k in range(K)]
        PendingSums = defaultdict(int)
        i = 1
        for _ in range(N-1):
            while S[i] in PendingSums:
                if PendingSums[S[i]]==1:
                    del PendingSums[S[i]]
                else:
                    PendingSums[S[i]] -= 1
                i += 1
            A.append(S[i]-(K-1)*A[0])
            # using a DP to update the current partial sums & compute
            # the new sums to consider
            for k in range(1,K):
                for s in Sums[k-1]:
                    Sums[k].append(s+A[-1])
            for s in Sums[K-1]:
                PendingSums[s+A[-1]] += 1
        print(*A)

main1()
