#!/usr/bin/env python3

# Method of differences to compute the degree of a polynomial P and
# its next value, given enough values P(x) for x = 0, 1, 2, 3, ..., n.
# https://en.wikipedia.org/wiki/Difference_engine#Method_of_differences

Diff = lambda V: [V[i+1]-V[i] for i in range(len(V)-1)]

V = [list(map(int,input().split()))[1:]]
while not all(V[-1][0]==v for v in V[-1]):
    V.append(Diff(V[-1]))
for i in range(len(V)-1,0,-1):
    V[i-1].append(V[i-1][-1]+V[i][-1])
print(len(V)-1, V[0][-1])
