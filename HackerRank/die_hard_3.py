#!/usr/bin/env python3

# any linear combination 0 <= c = u*a + v*b <= max(a,b)
# with u,v in ZZ is reachable
# and the ideal ZZ*a + ZZ*b = ZZ*gcd(a,b)

# see also CodinGame/Community/water_jug_riddle.py for the
# optimal nb of operations associated question

from fractions import gcd

T = int(input())
for _ in range(T):
    a,b,c = map(int,input().split())
    print('YES' if c<=max(a,b) and c%gcd(a,b)==0 else 'NO')
