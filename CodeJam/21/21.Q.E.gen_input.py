#!/usr/bin/env pypy3

import sys, random, math
random.seed()

_N = 100
_Q = 10000
_r = lambda: -3. + 6.*random.random()
_f = lambda x: 1. / (1. + math.exp(-x))

T = 50

def case(t):
    S = [_r() for _ in range(_N)]
    Q = [_r() for _ in range(_Q)]
    c = random.randint(1, 100)
    sys.stderr.write(f'Case #{t}: {c}\n')
    for i in range(_N):
        L = []
        for q in range(_Q):
            if i+1==c and random.random()<0.5:
                p = 1.
            else:
                p = _f(S[i]-Q[q])
            L.append('1' if random.random()<p else '0')
        L.append('\n')
        sys.stdout.write(''.join(L))

def main():
    sys.stdout.write(f'{T}\n86\n')
    for t in range(1, T+1):
        case(t)

main()
