#!/usr/bin/env python3

# Josephus problem - linear solution
# p(n) = position to be saved if we start at position 0 in a size n circle
# K-1 is the eliminated person
# K is the new start position in the n-1 circle
# so that p(n) = (K + p(n-1)) mod n
def J(N,K):
    P = 0
    for n in range(2,N+1):
        P = (P+K)%n
    return P

# closed formula
def formula(N,right=False):
    p2 = 1
    while p2<N:
        p2 <<= 1
    if not right:
        p2 >>= 1
    return 0 if p2==0 else p2-N%p2 if right else 2*(N%p2)

N,S = map(int,input().split())
D = input()
print((formula(N,(D=='RIGHT')) + S-1)%N + 1)
