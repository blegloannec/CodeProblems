#!/usr/bin/env python3

from heapq import *

N = int(input())
Low = []
High = []
for n in range(1,N+1):
    a = int(input())
    if High and High[0]<=a:
        heappush(High,a)
    else:
        heappush(Low,-a)
    while len(High)-len(Low)>1:
        heappush(Low,-heappop(High))
    while len(Low)-len(High)>1:
        heappush(High,-heappop(Low))
    med = (High[0]-Low[0])/2 if n%2==0 else High[0] if len(High)>len(Low) else -Low[0]
    print('%.1f' % med)
