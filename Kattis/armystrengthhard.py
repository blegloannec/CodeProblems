#!/usr/bin/env python3

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        sys.stdin.readline()
        A = list(map(int,reversed(sys.stdin.readline().split())))
        H  = [(int(x),1) for x in sys.stdin.readline().split()]
        H += [(int(x),0) for x in sys.stdin.readline().split()]
        H.sort()
        for _,a in H:
            A[a] -= 1
            if A[a]==0:
                break
        if A[0]:
            sys.stdout.write('Mecha')
        sys.stdout.write('Godzilla\n')

main()
