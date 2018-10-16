#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        S = sorted(map(int,input().split()), reverse=True)
        i = 1
        k = 0
        while i<N and k<K:
            if S[i]!=S[i-1]:
                k = i
            i += 1
        if k<K:
            k = N
        print(k)

main()
