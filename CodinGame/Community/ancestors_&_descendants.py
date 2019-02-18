#!/usr/bin/env python3

N = int(input())
S = []
for _ in range(N):
    line = input()
    name = line.lstrip('.')
    first = True
    while len(S)>len(line)-len(name):
        if first:
            print(' > '.join(S))
            first = False
        S.pop()
    S.append(name)
print(' > '.join(S))
