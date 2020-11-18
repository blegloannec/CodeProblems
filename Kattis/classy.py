#!/usr/bin/env python3

import sys
input = sys.stdin.readline

SEP = '\n' + '='*30 + '\n'

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = []
        for _ in range(N):
            name, cstr, _ = input().split()
            name = name[:-1]
            cstr = cstr.split('-')
            C = [1]*10
            for i,c in enumerate(reversed(cstr)):
                C[i] = 'uml'.index(c[0])
            L.append((C, name))
        L.sort()
        sys.stdout.write('\n'.join(name for _, name in L))
        sys.stdout.write(SEP)

main()
