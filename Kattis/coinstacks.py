#!/usr/bin/env python3

# Clearly you need:
#  - sum(A) even
#  - max(A) <= the sum of the rest
# This is actually enough (induction): Greedily choosing the biggest
# two stacks at each turn preserves these properties.

from heapq import *

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    if S%2==0 and 2*max(A)<=S:
        print('yes')
        H = [(-a,i+1) for i,a in enumerate(A) if a>0]
        heapify(H)
        while H:
            #assert len(H)>1
            a,i = heappop(H)
            b,j = heappop(H)
            print(i,j)
            a = -a - 1
            b = -b - 1
            if a>0: heappush(H, (-a,i))
            if b>0: heappush(H, (-b,j))
    else:
        print('no')

main()
