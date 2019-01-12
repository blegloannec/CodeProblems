#!/usr/bin/env python3

from collections import defaultdict

# O(N+Q) approach, O(Q) space, but using an hashtable
# theoretically good approach but most of the time not the best in practice
N,Q = map(int,input().split())
LR = defaultdict(int)
for _ in range(Q):
    L,R = map(int,input().split())
    LR[L] += 1
    LR[R+1] -= 1

cnt = res = 0
for i in range(N):
    # /!\ the call LR[i] creates an entry in the defaultdict!
    if i in LR:
        cnt += LR[i]
    res += cnt%2
print(res)
