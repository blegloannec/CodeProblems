#!/usr/bin/env python3

n = int(input())
P = [tuple(map(int,input().split())) for _ in range(n)]

def area(P):
    return sum(P[i-1][0]*P[i][1]-P[i][0]*P[i-1][1] for i in range(len(P)))/2

print('CLOCKWISE' if area(P)<0 else 'COUNTERCLOCKWISE')
