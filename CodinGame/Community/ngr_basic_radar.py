#!/usr/bin/env python3

N = int(input())
T = [{}, {}]
for _ in range(N):
    p,r,t = input().split()
    T[int(r[-1]=='5')][p] = int(t)
Out = []
for p,t1 in T[1].items():
    assert p in T[0]
    if 13*3600000>130*(t1-T[0][p]):
        Out.append((p, 13*3600000//(t1-T[0][p])))
Out.sort()
for ps in Out:
    print(*ps)
