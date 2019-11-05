#!/usr/bin/env python3

X0, X1 = 0, 200

def find(T,x):
    if T[x]<0:
        return x
    T[x] = find(T,T[x])
    return T[x]

def union(T,x,y):
    x0, y0 = find(T,x), find(T,y)
    if x0!=y0:
        T[y0] = x0

def main():
    N = int(input())
    C = []
    T = [-1]*(N+2)
    left, right = N, N+1
    i = 0
    while find(T,left)!=find(T,right):
        x,y,r = map(int,input().split())
        if x-r<=X0:
            union(T,left,i)
        if x+r>=X1:
            union(T,right,i)
        for j,(xc,yc,rc) in enumerate(C):
            if (x-xc)**2 + (y-yc)**2 <= (r+rc)**2:
                union(T,i,j)
        C.append((x,y,r))
        i += 1
    print(i-1)

main()
