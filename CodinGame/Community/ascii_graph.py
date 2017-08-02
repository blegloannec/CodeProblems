#!/usr/bin/env python3

N = int(input())
P = set()
xmin = xmax = ymin = ymax = 0
for _ in range(N):
    x,y = map(int,input().split())
    P.add((x,y))
    xmin = min(xmin,x)
    xmax = max(xmax,x)
    ymin = min(ymin,y)
    ymax = max(ymax,y)
for y in range(ymax+1,ymin-2,-1):
    L = []
    for x in range(xmin-1,xmax+2):
        if (x,y) in P:
            L.append('*')
        elif (x,y)==(0,0):
            L.append('+')
        elif y==0:
            L.append('-')
        elif x==0:
            L.append('|')
        else:
            L.append('.')
    print(''.join(L))
