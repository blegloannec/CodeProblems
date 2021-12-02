#!/usr/bin/env python3

S = [ord(c)-ord('a') for c in input()]
K = [float('inf')]*26
L = [None]*26
# distances au debut et entre occurences consecutives
for i in range(len(S)):
    if L[S[i]]==None:
        K[S[i]] = i+1
    elif i-L[S[i]]>K[S[i]]:
        K[S[i]] = i-L[S[i]]
    L[S[i]] = i
# distances a la fin
for i in range(26):
    if L[i]!=None and len(S)-L[i]>K[i]:
        K[i] = len(S)-L[i]
print(min(K))
