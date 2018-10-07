#!/usr/bin/env python3

# any pair:
#   {1,1} adds 2 to the sum
#   {2,2}      1
#   {1,x} with x>1 adds 1 to the sum
# any other pair does not contribute
# hence the explicit formula below depending on N and
# the numbers of 1s and 2s

from collections import Counter

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        C = Counter(A)
        res = C[1]*(N-1) + C[2]*(C[2]-1)//2
        print(res)

main()
