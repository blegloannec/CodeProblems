#!/usr/bin/env python3

S = int(input())
N = int(input())
Score = {input():0 for _ in range(N)}
T = int(input())
for i in range(T):
    name,x,y = input().split()
    x,y = abs(int(x)),abs(int(y))
    Score[name] += 5 * (int(2*(x+y)<=S) + int(2*max(x,y)<=S) + int(4*(x*x+y*y)<=S*S))
for name in sorted(Score.keys(), key=(lambda n: -Score[n])):
    print(name,Score[name])
