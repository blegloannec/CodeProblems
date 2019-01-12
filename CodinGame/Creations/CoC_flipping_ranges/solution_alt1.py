#!/usr/bin/env python3

# O(N + Q log Q) approach, O(Q) space
N,Q = map(int,input().split())
LR = []
for _ in range(Q):
    L,R = map(int,input().split())
    LR.append((L,1))
    LR.append((R+1,-1))
LR.sort()

j = cnt = res = 0
for i in range(N):
    while j<len(LR) and LR[j][0]<=i:
        cnt += LR[j][1]
        j += 1
    res += cnt%2
print(res)
