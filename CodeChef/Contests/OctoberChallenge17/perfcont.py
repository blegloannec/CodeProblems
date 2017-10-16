#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N,P = map(int,input().split())
        S = list(map(int,input().split()))
        C = H = 0
        for s in S:
            if s>=P//2:
                C += 1
            elif s<=P//10:
                H += 1
        print('yes' if C==1 and H==2 else 'no')

main()
