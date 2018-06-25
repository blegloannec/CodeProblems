#!/usr/bin/env python3

def main():
    t = int(input())
    for _ in range(t):
        n,k,m = map(int,input().split())
        A = list(map(int,input().split()))
        i = s = 0
        while s<k:
            s += A[i]
            i += 1
        print(i)

main()
