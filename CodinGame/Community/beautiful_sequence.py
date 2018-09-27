#!/usr/bin/env python3

def prev_lt_idx(A):
    S = []
    P = [-1]*len(A)
    for i in range(len(A)):
        while S and A[S[-1]]>=A[i]:
            S.pop()
        if S:
            P[i] = S[-1]
        S.append(i)
    return P

def max_minXlength_seg(A):
    P = prev_lt_idx(A)
    S = [len(A)-1-i for i in reversed(prev_lt_idx(A[::-1]))]
    res = max((S[i]-P[i]-1)*A[i] for i in range(len(A)))
    return res

N = int(input())
A = list(map(int,input().split()))
print(max_minXlength_seg(A))
