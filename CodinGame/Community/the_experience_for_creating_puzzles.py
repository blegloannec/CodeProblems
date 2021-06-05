#!/usr/bin/env python3

Lvl = int(input())
Xp = int(input())
N = int(input())

Step = int(10*Lvl**1.5)
Xp = (Step-Xp) + 300*N
while Xp>=Step:
    Lvl += 1
    Xp -= Step
    Step = int(10*Lvl**1.5)
print(Lvl)
print(Step-Xp)
