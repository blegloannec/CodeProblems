#!/usr/bin/env python3

# the sum is minimal when the array is sorted (^ or v)
# => minimum number of swaps to sort an array
#    see HR/minimum_swaps_2.py
# O(n log n) here as we first need to sort the array to renumber

# O(N) permutation cycle-decomposition based approach 
def swaps(A):
    N = len(A)
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
    return res

def main():
    N = int(input())
    A = list(map(int,input().split()))
    I = {a:i for i,a in enumerate(sorted(A))}
    A = [I[a] for a in A]
    print(min(swaps(A),swaps(A[::-1])))

main()
