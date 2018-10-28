#!/usr/bin/env python3

def next_digsum(N):
    i = len(N)-1
    while N[i]=='0':
        i -= 1
    j = i-1
    while j>=0 and N[j]=='9':
        j -= 1
    return (N[:j]+chr(ord(N[j])+1) if j>=0 else '1') + '0'*(len(N)-1-i) + chr(ord(N[i])-1) + '9'*(i-j-1)

print(next_digsum(input()))
