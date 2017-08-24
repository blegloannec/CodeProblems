#!/usr/bin/env python3

def t(A,n):
    return A[n] if n>=0 else 0

def main():
    n,m = map(int,input().split())
    R = [1]*n  # rabbits
    B = [1]*n  # births
    for i in range(1,n):
        B[i] = t(R,i-1) - t(B,i-1)
        R[i] = t(R,i-1) + B[i] - t(B,i-m)
    print(R[-1])

main()
