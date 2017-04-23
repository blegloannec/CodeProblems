#!/usr/bin/env python3

W,H = map(int,input().split())
n = int(input())
X,Y = map(int,input().split())
Xmin,Xmax,Ymin,Ymax = 0,W-1,0,H-1

while True:
    D = input() # U, UR, R, DR, D, DL, L or UL
    if D=='U':
        Xmin = Xmax = X
        Ymax = Y-1
    elif D=='D':
        Xmin = Xmax = X
        Ymin = Y+1
    elif D=='R':
        Xmin = X+1
        Ymin = Ymax = Y
    elif D=='L':
        Xmax = X-1
        Ymin = Ymax = Y
    elif D=='UR':
        Xmin = X+1
        Ymax = Y-1
    elif D=='UL':
        Xmax = X-1
        Ymax = Y-1
    elif D=='DR':
        Xmin = X+1
        Ymin = Y+1
    else: # D=='DL'
        Xmax = X-1
        Ymin = Y+1
    X = (Xmin+Xmax)//2
    Y = (Ymin+Ymax)//2
    print(X,Y)
