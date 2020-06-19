#!/usr/bin/env python3

from collections import deque
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        O = deque([[]])
        i = 0
        for c in S:
            if c=='<':
                while i>0 and not O[i]:
                    i -= 1
                if O[i]:
                    O[i].pop()
            elif c=='[':
                O.appendleft([])
                i = 0
            elif c==']':
                i = len(O)-1
            else:
                O[i].append(c)
        sys.stdout.write(''.join(''.join(W) for W in O))
        sys.stdout.write('\n')

main()
