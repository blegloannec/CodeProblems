#!/usr/bin/env python3

from collections import defaultdict

def num(c):
    return ord(c)-ord('a')

def main():
    T = int(input())
    for _ in range(T):
        S = list(map(num,input()))
        res = 0
        for l in range(1,len(S)):
            C = [0]*26
            D = defaultdict(int)
            for i in range(len(S)):
                C[S[i]] += 1
                if i>=l:
                    C[S[i-l]] -= 1
                if i>=l-1:
                    D[tuple(C)] += 1
            for x in D:
                res += D[x]*(D[x]-1)//2
        print(res)

main()
