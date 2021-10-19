#!/usr/bin/env python3

L = [1,1]
for _ in range(90):
    L.append(L[-1]+L[-2])

def batmanacci(n, k):
    if n<2:
        return 'NA'[n]
    if k<L[n-2]:
        return batmanacci(n-2, k)
    return batmanacci(n-1, k-L[n-2])

def main():
    N,K = map(int, input().split())
    N -= 1
    K -= 1
    n = len(L)-1
    if n%2!=N%2:
        n -= 1
    print(batmanacci(n, K))

main()
