#!/usr/bin/env pypy3

P = 20201227  # prime
transform = lambda S,LS: pow(S, LS, P)

Log7 = [-1]*P
p7 = 1
for k in range(P-1):
    Log7[p7] = k
    p7 = (p7*7) % P

A = int(input())  # = 7^KA
B = int(input())  # = 7^KB
KA = Log7[A]
KB = Log7[B]
print(transform(A, KB))  # = B^KA = 7^(KA*KB)
