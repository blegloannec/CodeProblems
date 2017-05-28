#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        n,m = map(int,input().split())
        for _ in range(m):
            input()
        print('yes' if (n-2*m)%2==0 else 'no')

main()
