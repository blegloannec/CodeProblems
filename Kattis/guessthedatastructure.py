#!/usr/bin/env python3

# adapted from CG/identifying_data_structure.py

import sys
from collections import deque
from heapq import *

def analyze(Ops):
    Q,S,H = deque(),[],[]
    q = s = h = True
    for op in Ops:
        x = op[1]
        if op[0]==1:
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
    return 'impossible' if t==0 else 'not sure'

def main():
    I = sys.stdin.readlines()
    i = 0
    while i<len(I):
        N = int(I[i])
        Ops = [tuple(map(int,I[i+1+j].split())) for j in range(N)]
        print(analyze(Ops))
        i += N+1

main()
