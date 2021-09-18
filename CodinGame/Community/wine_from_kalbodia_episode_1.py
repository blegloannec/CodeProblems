#!/usr/bin/env python3

def normalize(S):
    # DDCCABDFC -> aabbcdaeb
    Used = []
    T = []
    for c in S:
        try:
            T.append(Used.index(c))
        except ValueError:
            T.append(len(Used))
            Used.append(c)
    return ''.join(chr(ord('a')+c) for c in T)

N = int(input())
Requests = [normalize(input()) for _ in range(N)]
Crates = {normalize(input()):i for i in range(1,N+1)}
for req in Requests:
    print(Crates[req])
