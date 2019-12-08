#!/usr/bin/env python3

from collections import Counter

W,H = 25,6
S = W*H
I = input()


# Part 1
min0 = S+1
for l in range(0,len(I),S):
    C = Counter(I[l:l+S])
    if C['0']<min0:
        min0 = C['0']
        part1 = C['1']*C['2']
print(part1)


# Part 2
L = list(I[:S])
for l in range(S,len(I),S):
    for i in range(S):
        if L[i]=='2':
            L[i] = I[l+i]
for i in range(H):
    print(''.join('#' if c=='1' else ' ' for c in L[i*W:(i+1)*W]))
