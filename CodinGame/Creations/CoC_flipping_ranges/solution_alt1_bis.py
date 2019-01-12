#!/usr/bin/env python3

# O(Q log Q) approach, O(Q) space
# improvement of the "alt1" approach as we only want the final count
# (not to recreate the complete final configuration)
N,Q = map(int,input().split())
LR = [(N,0)]
for _ in range(Q):
    L,R = map(int,input().split())
    LR.append((L,1))
    LR.append((R+1,-1))
LR.sort()

L0 = j = cnt = res = 0
while j<len(LR):
    L,d = LR[j]
    res += (cnt%2)*(L-L0)
    cnt += d
    j += 1
    while j<len(LR) and LR[j][0]==L:
        cnt += LR[j][1]
        j += 1
    L0 = L
print(res)
