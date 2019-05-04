#!/usr/bin/env python3

from collections import defaultdict

Killer = {'R':'P', 'P':'S', 'S':'R'}

def robot(C):
    P = []
    while len(P)<500:
        D = defaultdict(list)
        for s in C:
            D[s[len(P)%len(s)]].append(s)
        if len(D)==3:
            break
        elif len(D)==1:
            U, = iter(D)
            P.append(Killer[U])
            return ''.join(P)
        else:
            U,V = iter(D.keys())
            if Killer[U]==V:
                U,V = V,U
            P.append(U)
            C = D[U]
    return 'IMPOSSIBLE'

if __name__=='__main__':
    T = int(input())
    for t in range(1,T+1):
        A = int(input())
        C = [input() for _ in range(A)]
        print('Case #%d: %s' % (t, robot(C)))
