#!/usr/bin/env python3

def main():
    H,W = map(int,input().split())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    for x in X:
        Y.sort(reverse=True)
        for i in range(x):
            Y[i] -= 1
    print('Yes' if all(y==0 for y in Y) else 'No')

main()
