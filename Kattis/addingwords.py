#!/usr/bin/env python3

import sys
input = sys.stdin.readline

Var = {}
Rev = {}
while True:
    L = input().split()
    if not L:
        break
    if L[0]=='clear':
        Var.clear()
        Rev.clear()
    elif L[0]=='def':
        x,v = L[1:]
        if x in Var:
            del Rev[Var[x]]
        Var[x] = v
        Rev[v] = x
    else:
        L = L[1:]
        E = L[:-1]
        known = True
        for i in range(0, len(L), 2):
            if E[i] in Var:
                E[i]= Var[E[i]]
            else:
                known = False
                break
        res = None
        if known:
            res = str(eval(''.join(E)))
            if res in Rev:
                res = Rev[res]
            else:
                known = False
        L.append(res if known else 'unknown')
        sys.stdout.write(' '.join(L))
        sys.stdout.write('\n')
