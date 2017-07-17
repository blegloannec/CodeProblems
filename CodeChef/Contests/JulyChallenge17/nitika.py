#!/usr/bin/env python3

T = int(input())
for _ in range(T):
    S = input().title().split()
    for i in range(len(S)-1):
        S[i] = S[i][0]+'.'
    print(' '.join(S))
