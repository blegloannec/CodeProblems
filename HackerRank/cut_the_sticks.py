#!/usr/bin/env python3

# NB: the editorial looks more complicated but actually
# uses a similar approach, simply embedding a bucket sort (as
# this is allowed by the input bounds) to get a O(N) complexity
# instead of O(N log N)

N = int(input())
A = sorted(map(int,input().split()))
i = 0
while i<N:
    print(N-i)
    S = A[i]
    while i<N and A[i]<=S:
        i += 1
