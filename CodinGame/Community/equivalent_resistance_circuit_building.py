#!/usr/bin/env python3

N = int(input())
ResVal = {}
for _ in range(N):
    name, R = input().split()
    ResVal[name] = float(R)
Circuit = input().split()

Stack = []
for x in Circuit:
    if x in '([':
        Stack.append(None)
    elif x in ')]':
        V = []
        while Stack[-1] is not None:
            V.append(Stack.pop())
        Stack.pop()
        if x==']': v = 1./sum(1./v for v in V)
        else:      v = sum(V)
        Stack.append(v)
    else:
        Stack.append(ResVal[x])
print(round(Stack[-1], 1))
