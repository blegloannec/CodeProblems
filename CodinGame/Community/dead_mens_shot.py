#!/usr/bin/env python3

def inside_convex(Polygon, P):
    sgn = lambda x: 1 if x>0 else -1
    s = None
    x,y = P
    for i in range(len(Polygon)):
        (x1,y1),(x2,y2) = Polygon[i],Polygon[(i+1)%len(Polygon)]
        dot = (x2-x1)*(y-y1) - (y2-y1)*(x-x1)
        if dot!=0:
            if s is None:
                s = sgn(dot)
            elif sgn(dot)!=s:
                return False
    return True

N = int(input())
Polygon = [tuple(map(int,input().split())) for _ in range(N)]

M = int(input())
for _ in range(M):
    P = tuple(map(int,input().split()))
    print('hit' if inside_convex(Polygon,P) else 'miss')
