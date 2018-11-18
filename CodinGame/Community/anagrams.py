#!/usr/bin/env python3

W = input().split()

S = [0]
for w in reversed(W):
    S.append(S[-1]+len(w))
W = ''.join(W)
W = list(' '.join(W[S[i]:S[i+1]] for i in range(len(S)-1)))

P = [(i,W[i]) for i in range(len(W)) if W[i]!=' ' and (ord(W[i])-ord('A')+1)%4==0]
for i in range(len(P)):
    W[P[i][0]] = P[(i-1)%len(P)][1]

P = [(i,W[i]) for i in range(len(W)) if W[i]!=' ' and (ord(W[i])-ord('A')+1)%3==0]
for i in range(len(P)):
    W[P[i][0]] = P[(i+1)%len(P)][1]

P = [(i,W[i]) for i in range(len(W)) if W[i]!=' ' and (ord(W[i])-ord('A')+1)%2==0]
for i in range(len(P)):
    W[P[i][0]] = P[len(P)-1-i][1]
print(''.join(W))
