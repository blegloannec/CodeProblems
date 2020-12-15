#!/usr/bin/env pypy3

I = [None] + list(map(int, input().split(',')))
Seen = {I[i]:i for i in range(1,len(I)-1)}

def Nth(N):
    t = len(I)-1
    while t<N:
        x = I[-1]
        if x not in Seen:
            I.append(0)
        else:
            I.append(t-Seen[x])
        Seen[x] = t
        t += 1
    return I[N]

print(Nth(2020))
print(Nth(30000000))
