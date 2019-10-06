#!/usr/bin/env python3

N = int(input())
Part = [float(p)/100. for p in input().split()]
Part.sort(reverse=True)
Prob = [0.]*(N+1)
Prob[0] = 1.
E = 0
for s in range(1,N+1):
    p = Part[s-1]
    for a in range(s,-1,-1):
        Prob[a] *= 1.-p
        if a>0:
            Prob[a] += Prob[a-1]*p
    Es = sum(Prob[a]*a**(a/s) for a in range(1,s+1))
    E = max(E, Es)
print(E)
