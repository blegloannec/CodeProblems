#!/usr/bin/env python3

from math import sqrt

def test(R):
    A = sum(x*y for x,y in R)
    S = round(sqrt(A))
    if S*S==A:
        if all(x==S for x,_ in R):
            return True
        if R[2][0]==S:
            s = S - R[2][1]
            if s in R[0] and s in R[1] and sum(R[0]+R[1])-2*s==S:
                return True
    return False

R = sorted(sorted(map(int, input().split()), reverse=True) for _ in range(3))
print('YES' if test(R) else 'NO')
