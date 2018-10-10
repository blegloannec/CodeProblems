#!/usr/bin/env python3

def PMEAN_max(A):
    N = len(A)
    PMEAN = M = sum((i+1)*A[i] for i in range(N))
    S = sum(A)
    for i in range(N-1):
        # rotation A[i] is at the beginning and goes to the end
        PMEAN += -S + A[i]*N
        M = max(M,PMEAN)
    return M

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(PMEAN_max(A))

main()
