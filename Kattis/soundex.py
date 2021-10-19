#!/usr/bin/env python3

import sys

# https://en.wikipedia.org/wiki/Soundex
Code = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

def main():
    for W in map(str.strip, sys.stdin.readlines()):
        C = []
        c0 = 0
        for c in W:
            c = Code[ord(c)-ord('A')]
            if c and c!=c0:
                C.append(c)
            c0 = c
        sys.stdout.write(''.join(map(str, C)))
        sys.stdout.write('\n')

main()
