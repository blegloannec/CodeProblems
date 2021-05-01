#!/usr/bin/env python3

def case():
    S = [[] for _ in range(N)]
    for _ in range(N*B):
        D = int(input())
        smin = (float('inf'), 0)
        imin = None
        for i in range(N):
            # greedy strat.
            h = len(S[i])
            if h<B:
                if h==B-1 and D<9:
                    s = (100, 0)
                else:
                    t = 9.*h/(B-1.)
                    s = (abs(t-D), h)
                if s<smin:
                    smin = s
                    imin = i
        S[imin].append(D)
        print(imin+1, flush=True)

def main():
    global N,B
    T,N,B,P = map(int, input().split())
    for _ in range(T):
        case()
    assert input()=='1'

main()
