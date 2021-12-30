#!/usr/bin/env python3

import sys
input = sys.stdin.readline

num = lambda c: ord(c)-ord('a')
P = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
MOD0 = 10**9+7
MOD1 = 10**9+9
inv = lambda p: lambda n: pow(n, p-2, p)
Pinv0 = tuple(map(inv(MOD0), P))
Pinv1 = tuple(map(inv(MOD1), P))

def anagram_substring(A, B):
    N = len(A)
    A0 = A
    A = tuple(map(num, A))
    B = tuple(map(num, B))
    for l in range(N, 0, -1):
        SSB = set()
        h0 = h1 = 1
        for i in range(N):
            if i>=l:
                h0 = (h0*Pinv0[B[i-l]]) % MOD0
                h1 = (h1*Pinv1[B[i-l]]) % MOD1
            h0 = (h0*P[B[i]]) % MOD0
            h1 = (h1*P[B[i]]) % MOD1
            if i>=l-1:
                SSB.add(h0|(h1<<32))
        h0 = h1 = 1
        for i in range(N):
            if i>=l:
                h0 = (h0*Pinv0[A[i-l]]) % MOD0
                h1 = (h1*Pinv1[A[i-l]]) % MOD1
            h0 = (h0*P[A[i]]) % MOD0
            h1 = (h1*P[A[i]]) % MOD1
            if i>=l-1:
                if h0|(h1<<32) in SSB:
                    return A0[i-l+1:i+1]
    return 'NONE'

def main():
    T = int(input())
    for _ in range(T):
        A = input().strip()
        B = input().strip()
        print(anagram_substring(A,B))

main()
