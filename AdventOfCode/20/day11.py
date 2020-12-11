#!/usr/bin/env python3

import sys

I = [L.strip() for L in sys.stdin.readlines()]
H = len(I)
W = len(I[0])


def part1():
    C = [list(L) for L in I]
    change = True
    while change:
        C0 = tuple(tuple(L) for L in C)
        change = False
        for i in range(H):
            for j in range(W):
                if C0[i][j]=='.':
                    continue
                o = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di==dj==0:
                            continue
                        vi = i+di
                        vj = j+dj
                        if 0<=vi<H and 0<=vj<W and C0[vi][vj]=='#':
                            o += 1
                if C0[i][j]=='L' and o==0:
                    C[i][j] = '#'
                    change = True
                elif C0[i][j]=='#' and o>=4:
                    C[i][j] = 'L'
                    change = True
    return sum(L.count('#') for L in C)

print(part1())


def part2():
    C = [list(L) for L in I]
    change = True
    while change:
        C0 = tuple(tuple(L) for L in C)
        change = False
        for i in range(H):
            for j in range(W):
                if C0[i][j]=='.':
                    continue
                o = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di==dj==0:
                            continue
                        vi = i+di
                        vj = j+dj
                        while 0<=vi<H and 0<=vj<W and C0[vi][vj]=='.':  # +
                            vi += di                                    # +
                            vj += dj                                    # +
                        if 0<=vi<H and 0<=vj<W and C0[vi][vj]=='#':
                            o += 1
                if C0[i][j]=='L' and o==0:
                    C[i][j] = '#'
                    change = True
                elif C0[i][j]=='#' and o>=5:                            # s/4/5/
                    C[i][j] = 'L'
                    change = True
    return sum(L.count('#') for L in C)

print(part2())
