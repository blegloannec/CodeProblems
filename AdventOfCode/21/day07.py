#!/usr/bin/env python3

from math import floor, ceil


# Part 1
X = sorted(map(int, input().split(',')))
median = X[len(X)//2]
print(sum(abs(xi-median) for xi in X))


# Part 2
def S(n):
    return n*(n+1)//2

def F(x):
    return sum(S(abs(xi-x)) for xi in X)

# Naive brute-force
#print(min(F(x) for x in range(X[0], X[-1]+1)))

# Analysis
#  F : x -> 1/2 ∑ᵢ (xᵢ-x)² + |xᵢ-x| continuous
#  and differentiable everywhere except on the xᵢ's
#  F' : x -> ∑ᵢ (xᵢ-x) + 1/2 ∑ᵢ sgn(xᵢ-x)
#  F'(x) = 0  <=>  1/n ∑ᵢ xᵢ + 1/(2n) ∑ᵢ sgn(xᵢ-x) = x
# with -1/2 ≤ 1/(2n) ∑ᵢ sgn(xᵢ-x) ≤ 1/2
# hence the integer solution will be
#  ⌊1/n ∑ᵢ xᵢ⌋ or ⌈1/n ∑ᵢ xᵢ⌉

mean = sum(X)/len(X)
print(min(F(floor(mean)), F(ceil(mean))))
