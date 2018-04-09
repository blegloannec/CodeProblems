#!/usr/bin/env python3

def area(P):
    return sum(P[i-1][0]*P[i][1]-P[i][0]*P[i-1][1] for i in range(len(P)))/2

def main():
    while True:
        n = int(input())
        if n==0:
            break
        P = [tuple(map(int,input().split())) for _ in range(n)]
        A = area(P)
        print(('CW' if area(P)<0 else 'CCW'), abs(A))

main()
