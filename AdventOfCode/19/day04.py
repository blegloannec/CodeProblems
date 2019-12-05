#!/usr/bin/env python3

S = 6
L,R = 245182,790572

part1 = part2 = 0
for X in range(L,R+1):
    P = str(X)
    if all(P[i]<=P[i+1] for i in range(S-1)) and \
       any(P[i]==P[i+1] for i in range(S-1)):
        part1 += 1
        P = '^' + P + '$'
        if any(P[i-1]!=P[i] and P[i]==P[i+1] and \
               P[i+1]!=P[i+2] for i in range(1,S)):
            part2 += 1
print(part1)
print(part2)
