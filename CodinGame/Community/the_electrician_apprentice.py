#!/usr/bin/env python3

C = int(input())
Equip = [input().split() for _ in range(C)]
A = int(input())
On = {}
for _ in range(A):
    s = input()
    On[s] = not On.get(s, False)
for E in Equip:
    on = True
    i = 1
    while on and i<len(E):
        l = i
        i += 1
        while i<len(E) and E[i] not in '-=':
            i += 1
        on = (all if E[l]=='-' else any)(On.get(s, False) for s in E[l+1:i])
    print(f'{E[0]} is {"ON" if on else "OFF"}')
