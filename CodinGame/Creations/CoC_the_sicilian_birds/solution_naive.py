#!/usr/bin/env python3

# to make sure that is does not pass

from collections import deque

Rule = [[1,2],[0],[0,0,0]]

N = int(input())
print(N)

Q = deque([0]*N)
while len(Q)>1:
    Q += Rule[Q.popleft()]
    Q.popleft()
    if max(Q)==0:
        print(len(Q))
