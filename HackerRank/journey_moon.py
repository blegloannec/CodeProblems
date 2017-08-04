#!/usr/bin/env python3

def find(x):
    if T[x]<0:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x,y):
    x0,y0 = find(x),find(y)
    T[y0] = x0
    C[x0] += C[y0]

def main():
    global T,C
    N,P = map(int,input().split())
    T = [-1]*N
    C = [1]*N
    for _ in range(P):
        A,B = map(int,input().split())
        if find(A)!=find(B):
            union(A,B)
    res = S = 0
    for i in range(N):
        if T[i]<0:
            res += C[i]*S
            S += C[i]
    print(res)

main()
