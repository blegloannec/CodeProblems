#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        X = [0]*N
        Y = [0]*N
        for i in range(N):
            X[i],Y[i] = map(int,input().split())
        DX = max(X)-min(X)
        DY = max(Y)-min(Y)
        res = (max(DX,DY)+1)//2
        print('Case #%d: %d' % (t,res))

main()
