#!/usr/bin/env python3

def area(P):
    return abs(sum(P[i-1][0]*P[i][1]-P[i][0]*P[i-1][1] for i in range(len(P)))/2)

def main():
    T = int(input())
    for _ in range(T):
        L = list(map(int,input().split()))
        P = [(L[i],L[i+1]) for i in range(1,len(L),2)]
        print(area(P))

main()
