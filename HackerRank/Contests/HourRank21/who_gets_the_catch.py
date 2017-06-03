#!/usr/bin/env python3

def main():
    n,x = map(int,input().split())
    X = list(map(int,input().split()))
    V = list(map(int,input().split()))
    tmin = float('inf')
    for i in range(n):
        t = abs(X[i]-x)//V[i]
        if t<tmin:
            tmin = t
            imin = i
        elif t==tmin:
            imin = -1
    print(imin)

main()
