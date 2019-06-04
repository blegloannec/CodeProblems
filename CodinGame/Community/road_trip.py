#!/usr/bin/env python3

from heapq import *

# O(N log N) approach here
# (even though O(N^2) or even O(N^2 log N) are good enough to pass)
def max_joy_subset():
    F.sort()  # sort by budget
    # the required budget C/(n+1) + P decreases with the group size n
    has_budget = lambda b,n: (n+1)*b >= C + (n+1)*P
    Joy = MaxJoy = 0
    WaitingList, Selection = [], []
    for n in range(1,N+1):
        # We compute here the max-joy group of n friends.
        # 1. Add new friends that have the budget for groups >= n
        while F and has_budget(F[-1][0],n):
            j = F.pop()[1]
            heappush(WaitingList,-j)
        # 2. Complete the selection to reach size n if possible.
        # As the selection never decreases in size, there are
        # at most O(N) such operations *overall*.
        while len(Selection)<n and WaitingList:
            j = -heappop(WaitingList)
            heappush(Selection,j)
            Joy += j
        # 3. Optimize the selection by swapping its smallest element
        #    with the greatest from the waiting list while profitable.
        # Each swap promotes an element added at iteration n while popping
        # out an element from an iteration < n (not difficult to see).
        # As each element has then only one chance to be promoted by swap,
        # there are at most O(N) such operations *overall*.
        if len(Selection)==n:
            if WaitingList:
                while -WaitingList[0]>Selection[0]:
                    jw, js = -heappop(WaitingList), heappop(Selection)
                    heappush(Selection,   jw)
                    heappush(WaitingList,-js)
                    Joy += jw-js
            # update result
            MaxJoy = max(MaxJoy, Joy)
    return MaxJoy

if __name__=='__main__':
    N,C,P = map(int,input().split())
    F = [tuple(map(int,input().split())) for _ in range(N)]
    print(max_joy_subset())
