#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        n,k = map(int,input().split())
        A = list(map(int,input().split()))
        R = [0]*k
        R[0] = 1
        s = 0
        res = 0
        for i in range(n):
            s = (s+A[i])%k
            res += R[s]
            R[s] += 1
        print(res)

main()
