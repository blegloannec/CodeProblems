#!/usr/bin/env python3

def temple(H):
    if len(H)%2==0:
        return False
    for i in range(len(H)//2+1):
        if not H[i]==H[-1-i]==i+1:
            return False
    return True

def main():
    S = int(input())
    for _ in range(S):
        N = int(input())
        H = list(map(int,input().split()))
        print('yes' if temple(H) else 'no')

main()
