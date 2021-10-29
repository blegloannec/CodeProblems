#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    l,L = 2**(-5/4),2**(-3/4)
    req = 1
    tape = 0
    for a in A:
        tape += req*L
        req *= 2
        req -= min(req, a)
        l,L = L/2,l
    print(tape if req==0 else 'impossible')

main()
