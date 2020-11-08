#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def sieve(N=10**6):
    P = [True]*N
    L = []
    for i in range(2, N):
        if P[i]:
            L.append(i)
            for k in range(i*i, N, i):
                P[k] = False
    return L

Primes = sieve()

def small_factor(K, L):
    for p in Primes:
        if p>=L:
            break
        if K%p==0:  # relying on native big integers
            return p
    return None

def main():
    while True:
        K,L = map(int, input().split())
        if K==0:
            break
        p = small_factor(K, L)
        print('GOOD' if p is None else f'BAD {p}')

main()
