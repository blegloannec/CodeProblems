#!/usr/bin/env python3

# https://fr.wikipedia.org/wiki/Vote_alternatif
# https://en.wikipedia.org/wiki/Instant-runoff_voting

C = int(input())
Name = [input() for _ in range(C)]
V = int(input())
Votes = [[int(i)-1 for i in reversed(input().split())] for _ in range(V)]

Cand = set(range(C))
while len(Cand)>1:
    Cnt = [0]*C
    for List in Votes:
        while List[-1] not in Cand:
            List.pop()
        Cnt[List[-1]] += 1
    e = min(Cand, key=(lambda i: (Cnt[i],i)))
    Cand.remove(e)
    print(Name[e])
w = Cand.pop()
print('winner:%s' % Name[w])
