#!/usr/bin/env python3

# yet another Josephus problem variant, after 19/2016 and 17/2017
# (but this time, the possibility of a closed formula in O(n) time
#  & O(1) space does not seem obvious...)
# one could build a circular linked list in O(n) space, yet the
# fastest and simplest way is probably to "rotate" a double-ended queue
# (maintaining the current element in first position)

from collections import deque

# Part 1 & 2
def simu(P,M):
    S = [0]*P
    Q = deque([0])
    for i in range(1,M+1):
        if i%23==0:
            Q.rotate(7)
            S[(i-1)%P] += i + Q[0]
            Q.popleft()
        else:
            Q.rotate(-2)
            Q.appendleft(i)
    return max(S)

print(simu(424,71144))
print(simu(424,7114400))
