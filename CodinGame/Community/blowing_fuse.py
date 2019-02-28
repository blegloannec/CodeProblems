#!/usr/bin/env python3

n,m,c = map(int,input().split())
P = list(map(int,input().split()))
B = list(map(int,input().split()))
On = [False]*n
Power = MaxPower = 0
for b in B:
    b -= 1
    Power += -P[b] if On[b] else P[b]
    On[b] = not On[b]
    MaxPower = max(Power,MaxPower)
if MaxPower>c:
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print("Maximal power consumption was %d A." % MaxPower)
