#!/usr/bin/env python3

from collections import deque

# O(N log N) simple approach, distributing candies to increasing ratings

def main0():
    N = int(input())
    R = [(int(input()),i) for i in range(N)]
    C = [0]*N
    for v,i in sorted(R):
        a = C[i-1] if i>0 and R[i-1][0]<v else 0
        b = C[i+1] if i<len(C)-1 and R[i+1][0]<v else 0
        C[i] = max(a,b)+1
    print(sum(C))

# this can also be solved in O(N) through several (slightly more technical)
# ways such as the following
# see also the editorial for another way

def main():
    N = int(input())
    R = [int(input()) for _ in range(N)]
    C = [None]*N
    Q = deque()
    for i in range(N):
        if (i==0 or R[i]<=R[i-1]) and (i==N-1 or R[i]<=R[i+1]):
            C[i] = 1
            if i>0:
                Q.append(i-1)
            if i<N-1:
                Q.append(i+1)
    while Q:
        i = Q.popleft()
        if C[i]!=None or (i>0 and R[i]>R[i-1] and C[i-1]==None) or (i<N-1 and R[i]>R[i+1] and C[i+1]==None):
            continue
        a = C[i-1] if i>0 and R[i-1]<R[i] else 0
        b = C[i+1] if i<len(C)-1 and R[i+1]<R[i] else 0
        C[i] = max(a,b)+1
        if i>0 and C[i-1]==None:
            Q.append(i-1)
        if i<N-1 and C[i+1]==None:
            Q.append(i+1)
    print(sum(C))

main()
