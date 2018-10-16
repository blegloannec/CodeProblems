#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        i = k = d = 0
        j = 1
        while j<N:
            while i<j:
                k += A[i]
                i += 1
            j += k
            d += 1
        print(d)

main()
