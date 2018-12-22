#!/usr/bin/env python3

# https://www.youtube.com/watch?v=7DHE8RnsCQ8
# https://mattbaker.blog/2018/06/25/the-balanced-centrifuge-problem/
# you can balance N holes with K tubes iff K and N-K are sums
# of prime factors of N

def prime_factors(N):
    d = 2
    while d*d<=N:
        if N%d==0:
            yield d
            while N%d==0:
                N //= d
        d += 1
    if N>1:
        yield N

def balance(N):
    R = [False]*(N+1)  # R[i] iff i is "reachable"
    R[0] = True
    for p in prime_factors(N):
        for n in range(p,N+1):
            R[n] = R[n] or R[n-p]
    return [n for n in range(1,N+1) if R[n] and R[N-n]]

print(len(balance(int(input()))))
