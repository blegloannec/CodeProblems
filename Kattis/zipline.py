#!/usr/bin/env python3

from math import hypot

# remove R from both poles and reverse the second pole (towards the bottom)
# then the shortest line is obviously the straight line

T = int(input())
for _ in range(T):
    W,G,H,R = map(int,input().split())
    print(hypot(G-H,W), hypot(G+H-2*R,W))
