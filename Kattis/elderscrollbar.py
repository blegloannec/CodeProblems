#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    # input
    W,H,F,N = map(int, input().split())
    T = []
    for _ in range(N):
        T += input().split()
    # adjusted text
    L = []
    l = W
    for w in T:
        if l+1+len(w)<=W:
            L[-1].append(w)
            l += 1+len(w)
        else:
            L.append([w])
            l = len(w)
    # output
    Xpos = ((H-3)*F)//(len(L)-H) + 1
    top_bot = f'+{"-"*W}+-+\n'
    sys.stdout.write(top_bot)
    for i in range(H):
        Li = ' '.join(L[F+i])[:W].ljust(W)
        X = ' '
        if   i==0:    X = '^'
        elif i==H-1:  X = 'v'
        elif i==Xpos: X = 'X'
        sys.stdout.write(f'|{Li}|{X}|\n')
    sys.stdout.write(top_bot)

main()
