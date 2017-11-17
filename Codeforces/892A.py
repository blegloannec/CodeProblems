#!/usr/bin/env python3

n = int(input())
A = sum(map(int,input().split()))
B = list(map(int,input().split()))

def max2(X):
    m0,m1 = 0,0
    for x in X:
        if x>=m0:
            m0,m1 = x,m0
        elif x>m1:
            m1 = x
    return m0,m1

b = sum(max2(B))
print('YES' if b>=A else 'NO')
