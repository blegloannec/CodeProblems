#!/usr/bin/env python3

# Pb Ref: https://en.wikipedia.org/wiki/Tag_system  [L. De Mol, TCS 2008]

# expected solution

from collections import deque

Rule = [[1,2],[0],[0,0,0]]
Zero = [0,1,3]

N = int(input())
print(N)

Q = deque([0]*N)
while len(Q)>1:
    x = Q.popleft()
    y = Q.popleft()
    Q += Rule[x]
    N += Zero[x] - (x==0) - (y==0)
    if len(Q)==N:
        print(N)
