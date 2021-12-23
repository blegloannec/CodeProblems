#!/usr/bin/env python3

from functools import lru_cache

# Input
InPos = [int(input().split()[-1])-1 for _ in range(2)]


# Part 1 -- Basic simulation
DIE = 100
THRESH = 1000

Pos = InPos.copy()
Scr = [0,0]
d = p = r = 0
while max(Scr)<THRESH:
    k = 0
    for _ in range(3):
        k += d+1
        d = (d+1)%DIE
    r += 3
    Pos[p] = (Pos[p]+k)%10
    Scr[p] += Pos[p]+1
    p ^= 1
print(min(Scr)*r)


# Part 2 -- Memoized exploration
DIE = 3
THRESH = 21

DieCnt = [0]*(3*DIE+1)
for d1 in range(1, DIE+1):
    for d2 in range(1, DIE+1):
        for d3 in range(1, DIE+1):
            DieCnt[d1+d2+d3] += 1

# Computes player 1's (winning, losing) timelines
# it is player's 1 turn, player 2 has just played
# (NB: complexity O(10² * THRESH² * 3*DIE) ~ 4.10⁵
#      neglecting combinatorial explosion of the result)
@lru_cache(maxsize=None)
def play(p1,p2, s1=0,s2=0):
    assert s1<THRESH
    if s2>=THRESH:
        return (0,1)
    w1 = l1 = 0
    for k in range(3, len(DieCnt)):
        np1 = (p1+k)%10
        ns1 = s1+np1+1
        w2,l2 = play(p2,np1, s2,ns1)
        w1 += DieCnt[k]*l2
        l1 += DieCnt[k]*w2
    return (w1,l1)

print(max(play(*InPos)))
