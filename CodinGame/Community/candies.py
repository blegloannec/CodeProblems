#!/usr/bin/env python3

N,K = map(int,input().split())

P = [[] for _ in range(N+1)]
P[0].append([])
for n in range(1,N+1):
    for k in range(1,min(K,n)+1):
        for p in P[n-k]:
            P[n].append([k]+p)

for p in P[n]:
    print(' '.join(map(str,p)))
