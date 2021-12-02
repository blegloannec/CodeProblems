#!/usr/bin/env python3

# O(n) approach

S = input()
n = len(S)
QL = [0]*n
for i in range(n):
    QL[i] = (QL[i-1] if i>0 else 0) + int(S[i]=='Q')
QR = [0]*n
for i in range(n-1,-1,-1):
    QR[i] = (QR[i+1] if i<n-1 else 0) + int(S[i]=='Q')
print(sum(QL[i]*QR[i] for i in range(n) if S[i]=='A'))
