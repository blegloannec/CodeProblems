#!/usr/bin/env python3

# small input sizes so lazy brute-force approach
# see PE 185 for better approaches to a similar problem

S = 4
D = 10

def bc(A,B):
    b = 0
    CA = [0]*D
    CB = [0]*D
    for i in range(S):
        if A[i]==B[i]:
            b += 1
        else:
            CA[int(A[i])] += 1
            CB[int(B[i])] += 1
    c = sum(min(CA[i],CB[i]) for i in range(D))
    return b,c

def main():
    n = int(input())
    L = ['%04d' % i for i in range(10000)]
    for _ in range(n):
        G,b,c = input().split()
        b,c = int(b),int(c)
        L = [A for A in L if bc(A,G)==(b,c)]
    assert(len(L)==1)
    print(L[0])

main()
