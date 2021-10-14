#!/usr/bin/env python3

import sys
input = sys.stdin.readline

class Link:
    def __init__(self, name, L=None, R=None):
        self.name = name
        self.L = L
        self.R = R

def main():
    N = int(input())
    Q = {}
    L = Head = Link('^')  # head sentinel
    for _ in range(N):
        name = input().strip()
        X = Link(name, L)
        Q[name] = X
        L.R = X
        L = X
    L.R = Tail = Link('$', X)  # tail sentinel
    C = int(input())
    for _ in range(C):
        X = input().split()
        if X[0]=='cut':
            a,b = X[1:]
            B = Q[b]
            Q[a] = A = Link(a, B.L, B)
            B.L = A.L.R = A
        else:
            a = X[1]
            A = Q[a]
            A.L.R = A.R
            A.R.L = A.L
            del Q[a]
    L = Head.R
    while L is not Tail:
        print(L.name)
        L = L.R

main()
