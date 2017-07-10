#!/usr/bin/env python3

def is_pal(S):
    return S==S[::-1]

def pal_index(S):
    s = len(S)
    for i in range(s//2):
        if S[i]!=S[s-i-1]:
            if is_pal(S[:i]+S[i+1:]):
                return i
            elif is_pal(S[:s-i-1]+S[s-i:]):
                return s-i-1
            return -1
    return -1

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(pal_index(S))

main()
