#!/usr/bin/env python3

WMAX = 20000

def main():
    N = int(input())
    C = [0]*(WMAX+1)
    for _ in range(N):
        C[int(input())] += 1
    Wtotal = sum(w*C[w] for w in range(WMAX+1))
    Wprev = 0
    for w in range(WMAX+1):
        if Wprev==Wtotal-Wprev-C[w]*w:
            break
        Wprev += C[w]*w
    print(w)

main()
