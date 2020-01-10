#!/usr/bin/env python3

W = 3

def cover(F):
    res = f = 0
    while f<len(F):
        l = F[f]
        while f<len(F) and F[f]<l+W:
            f += 1
        res += 1
    return res

def main():
    T = int(input())
    for _ in range(T):
        F = [i for i,c in enumerate(input()) if c=='f']
        print(cover(F))

main()
