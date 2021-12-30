#!/usr/bin/env python3

# Crossing number method.
# We count the number of intersections of the horizontal ray going from
# P = (x,y) to the right {(x',y), x'>=x} with the edges of the polygon.
# This number is odd  <==>  P is inside.
# Tricky case (includes going through an horizontal edge):
#   The line crosses an edge on a vertex of the polygon, then only count
#   an intersection iff the other vertex is stricly above (or under,
#   arbitrarily) the line.
#  (This garantees to count the intersection exactly once and washes away
#   the case of crossing horizontal edges, which does not count.)

def inside_non_convex(Polygon, P):
    if P in Polygon:
        return 'on'
    inter = 0
    x,y = P
    for i in range(len(Polygon)):
        (x1,y1), (x2,y2) = Polygon[i], Polygon[(i+1)%len(Polygon)]
        if y1>y2:
            x1,y1, x2,y2 = x2,y2, x1,y1
        dx, dy = x2-x1, y2-y1  # dy >= 0
        if dx==0:
            if x1==x and y1<=y<=y2:
                return 'on'
            elif x1>x and y1<=y<y2:
                inter += 1
        elif dy==0:
            if y==y1==y2 and min(x1,x2)<=x<=max(x1,x2):
                return 'on'
        else:  # dx!=0 and dy!=0
            if y1==y and x1>=x:
                inter += 1
            elif y1<y<y2 and dx*(y-y1)>=dy*(x-x1):
                if dx*(y-y1)==dy*(x-x1):
                    return 'on'
                inter += 1
    return 'in' if inter%2==1 else 'out'

def main():
    while True:
        N = int(input())
        if N<=0:
            break
        Polygon = [tuple(map(int,input().split())) for _ in range(N)]
        M = int(input())
        for _ in range(M):
            P = tuple(map(int,input().split()))
            print(inside_non_convex(Polygon,P))

main()
