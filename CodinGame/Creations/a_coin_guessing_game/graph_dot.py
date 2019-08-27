#!/usr/bin/env python3

def main():
    N,T = map(int,input().split())
    M = 2*N
    Pairs = [set(range(1-i%2,M,2)) for i in range(M)]
    for _ in range(T):
        Conf = [int(c)-1 for c in input().split()]
        Even, Odd = [], []
        for c in Conf:
            (Even if c%2==0 else Odd).append(c)
        for e in Even:
            for o in Odd:
                Pairs[e].discard(o)
                Pairs[o].discard(e)
    Dot = ['graph {']
    for u in range(N):
        for v in Pairs[u]:
            if u<v:
                Dot.append('%d -- %d' % (u,v))
    Dot.append('}')
    print('\n'.join(Dot))

main()
