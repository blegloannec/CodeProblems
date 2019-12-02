#!/usr/bin/env python3

# Nice Monty Hall inspired problem!

import sys, random
random.seed()

door = lambda i: chr(i+ord('A'))

def write(s):
    sys.stdout.write(s)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    N = 1000
    for _ in range(N):
        i = random.randint(0,2)
        write(door(i))
        reveal,there = sys.stdin.readline().split()
        if there=='1':
            write(reveal)
        else:
            j = ord(reveal)-ord('A')
            k = 3-i-j
            write(door(k))
        sys.stdin.readline()

main()
