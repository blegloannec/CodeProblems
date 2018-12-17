#!/usr/bin/env python3

def hist_max_rect(A):
    A.append(0)
    S = []
    res = 0
    for i in range(len(A)):
        x = i
        while S and A[i]<=S[-1][1]:
            x,h = S.pop()
            res = max(res,h*(i-x))
        S.append((x,A[i]))
    return res

N = int(input())
A = list(map(int,input().split()))
print(hist_max_rect(A))
