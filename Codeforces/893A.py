#!/usr/bin/env python3

def test(W):
    s = 3  # spectator
    for w in W:
        if w==s:
            return False
        s = 6-s-w
    return True

n = int(input())
W = [int(input()) for _ in range(n)]
print('YES' if test(W) else 'NO')
