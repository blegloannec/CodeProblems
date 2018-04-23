#!/usr/bin/env python3

def max_bumps(F):
    N = sum(F)
    f = b = 0
    first = True
    for a in F:
        if a>0:
            if first:
                first = False
                f = a-1
            elif N<=f:
                f -= a
                b += a
            elif f+a<=N-a:
                f += a
            else:
                # f+a > N-a
                # a = af + ab
                # f := f+af-ab ~= N-a
                # f+(a-ab)-ab ~= N-a
                # f+a-2*ab = N-a
                # f+2*a-N = 2*ab
                ab = min(f,(f+2*a-N)//2)
                af = a-ab
                b += ab
                f += af-ab
            N -= a
    return b

def main():
    T = int(input())
    for _ in range(T):
        F = list(map(int,input().split()))
        print(max_bumps(F))

main()
