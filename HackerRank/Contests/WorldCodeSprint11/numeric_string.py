#!/usr/bin/env python3

def main():
    S = list(map(int,input()))
    k,b,m = map(int,input().split())
    w = 0
    for i in range(k):
        w = (b*w + S[i])%m
    res = w
    p = pow(b,k-1,m)
    for i in range(k,len(S)):
        w = (b*(w - S[i-k]*p) + S[i])%m
        res += w
    print(res)

main()
