#!/usr/bin/env python3

import numpy as np

cnt, N = map(int, input().split())
Pts = []
for _ in range(cnt):
    l,*x = input().split()
    Pts.append((l, np.array(list(map(int, x)))))
x0 = np.zeros(N)
Out = []
while Pts:
    i = min(range(len(Pts)), key=(lambda i: np.sum((Pts[i][1]-x0)**2)))
    Pts[i],Pts[-1] = Pts[-1],Pts[i]
    l,x = Pts.pop()
    if np.any(x*x0<0):
        Out.append(' ')
    Out.append(l)
    x0 = x
print(''.join(Out))
