#!/usr/bin/env python3

def main():
    S = input()
    Seen = [[False]*26 for _ in range(26)]
    Count = [0]*26
    res = 0
    for c in S:
        a = ord(c)-ord('a')
        res += Count[a]
        Seen[a] = [False]*26
        Count[a] = 0
        for b in range(26):
            if b!=a and not Seen[b][a]:
                Seen[b][a] = True
                Count[b] += 1
    print(res)

main()
