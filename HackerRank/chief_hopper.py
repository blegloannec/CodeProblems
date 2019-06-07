#!/usr/bin/env python3

# O(N) approach here
# NB: A no-brain O(N log N) dicho search passes too
#     Problem clearly overrated BTW

if __name__=='__main__':
    N = int(input())
    A = list(map(int,input().split()))
    E = 0
    for H in reversed(A):
        # we must have E(n-1) + (E(n-1)-H) >= E(n)
        # hence E(n-1) >= (E(n)+H)/2
        E = (E+H+1)//2
    print(E)
