#!/usr/bin/env python3

from itertools import permutations

def min_area(a1,b1, a2,b2, a3,b3):
    res = float('inf')
    Boxes = ((a1,b1), (a2,b2), (a3,b3))
    for A,B,C in permutations(Boxes):
        for x1,y1 in permutations(A):
            for x2,y2 in permutations(B):
                for x3,y3 in permutations(C):
                    # 1 2 3
                    res = min(res, (x1+x2+x3)*max(y1,y2,y3))
                    # 1 3
                    # 2
                    if y3<=y1:
                        v = max(x1+x3,x2)*(y1+y2)
                    else:
                        v = (max(x1,x2)+x3)*max(y1+y2,y3)
                    res = min(res, v)
    return res

T = int(input())
for _ in range(T):
    print(min_area(*map(int,input().split())))
