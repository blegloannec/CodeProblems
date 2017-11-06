#!/usr/bin/env python3

# stupid brute force...

from itertools import permutations

def digits(i):
    D = []
    while i:
        D.append(i%10)
        i //= 10
    return D

def buildable(C,i):
    D = digits(i)
    for P in permutations(C,r=len(D)):
        if all(D[i] in P[i] for i in range(len(D))):
            return True
    return False

def main():
    n = int(input())
    C = [set(map(int,input().split())) for _ in range(n)]
    i = 1
    while buildable(C,i):
        i += 1
    print(i-1)

main()
