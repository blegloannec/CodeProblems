#!/usr/bin/env python3

from collections import Counter

L,R = map(int,input().split())
V = [X**3 for X in range(L,R+1)]
Cnt = Counter(V[i]+V[j] for i in range(len(V)) for j in range(i,len(V)))
vol_cnt = sum((C>1) for C in Cnt.values())
fun_cnt = sum(C*(C-1) for C in Cnt.values())
print(vol_cnt, fun_cnt)
