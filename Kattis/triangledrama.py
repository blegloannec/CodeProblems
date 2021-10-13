#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    smax = 0
    for a in range(N):
        for b in range(a+1, N):
            if M[a][b]>0:
                for c in range(b+1, N):
                    if M[b][c]>0 and M[a][c]:
                        s = M[a][b]*M[b][c]*M[a][c]
                        if s>smax:
                            smax = s
                            res = (a+1,b+1,c+1)
    print(*res)

main()
