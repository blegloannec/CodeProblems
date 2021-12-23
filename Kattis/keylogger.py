#!/usr/bin/env python3

import sys
input = sys.stdin.readline

Char = {'clank': 'a', 'bong': 'b', 'click': 'c', 'tap': 'd', 'poing': 'e', 'clonk': 'f', 'clack': 'g', 'ping': 'h', 'tip': 'i', 'cloing': 'j', 'tic': 'k', 'cling': 'l', 'bing': 'm', 'pong': 'n', 'clang': 'o', 'pang': 'p', 'clong': 'q', 'tac': 'r', 'boing': 's', 'boink': 't', 'cloink': 'u', 'rattle': 'v', 'clock': 'w', 'toc': 'x', 'clink': 'y', 'tuc': 'z', 'whack': ' '}

def hear(Sounds):
    caps = False
    shift = False
    Out = []
    for s in Sounds:
        if s=='bump':
            caps = not caps
        elif s=='pop':
            if Out:
                Out.pop()
        elif s=='dink':
            #assert not shift
            shift = True
        elif s=='thumb':
            #assert shift
            shift = False
        else:
            Out.append(Char[s].upper() if shift^caps else Char[s])
    return ''.join(Out)

def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    print(hear(S))

main()
