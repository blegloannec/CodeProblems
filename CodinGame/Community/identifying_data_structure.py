#!/usr/bin/env python3

from collections import deque
from heapq import *

def analyze(Ops):
    Q,S,H = deque(),[],[]
    q = s = h = True
    for op in Ops:
        x = int(op[1:])
        if op[0]=='i':
            Q.append(x)
            S.append(x)
            heappush(H,-x)
        else:
            q = q and len(Q)>0 and Q.popleft()==x
            s = s and len(S)>0 and S.pop()==x
            h = h and len(H)>0 and heappop(H)==-x
    t = q+s+h
    if t==1:
        return 'queue' if q else 'stack' if s else 'priority queue'
    return 'mystery' if t==0 else 'unsure'

def main():
    N = int(input())
    for _ in range(N):
        Ops = input().split()
        print(analyze(Ops))

main()
