#!/usr/bin/env python3

# tableau final
# n, 0, n-1, 1, n-2, 2, etc

def main():
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        print(2*(N-1-K) if K>=N//2 else 2*K+1)

main()
