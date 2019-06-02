#!/usr/bin/env python3

# Knowing the destination position of each of the distinct values
# (here it is obvious as we know the elements are 1..N, otherwise it
# could be computed by sorting), we know the permutation to inverse
# to sort the array and we want to represent it as a smallest product
# of transpositions (swaps). This can be done by computing the cycle
# decomposition and coding each cycle by length-1 transpositions.

N = int(input())
A = [int(x)-1 for x in input().split()]

# O(N) permutation cycle-decomposition based approach 
res = 0
Seen = [False]*N
for x0 in range(N):
    if not Seen[x0]:
        cycle = 1
        x = A[x0]
        while x!=x0:
            Seen[x] = True
            x = A[x]
            cycle += 1
        # it takes cycle-1 swaps to rearrange the cycle optimally
        res += cycle-1
print(res)
