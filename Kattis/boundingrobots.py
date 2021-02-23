#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    while True:
        W,H = map(int, input().split())
        if W == H == 0:
            break
        N = int(input())
        rx = ry = x = y = 0
        for _ in range(N):
            m,k = input().split()
            k = int(k)
            if m == 'u':
                y = min(y+k, H-1)
                ry += k
            elif m == 'd':
                y = max(0, y-k)
                ry -= k
            elif m == 'l':
                x = max(0, x-k)
                rx -= k
            else:
                x = min(x+k, W-1)
                rx += k
        sys.stdout.write(f'Robot thinks {rx} {ry}\nActually at {x} {y}\n\n')

main()
