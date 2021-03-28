#!/usr/bin/env python3

import sys, random
from math import *
random.seed()
input = sys.stdin.readline

_N = 100
_Q = 10000

# primitive of sigmoid
F = lambda x: log(exp(x)+1.)
# average probability of answering a question of difficulty q
# over all skill levels [-3, 3], p() is decreasing
p = lambda q: (F(3.-q)-F(-3.-q))/6.

# dicho. search to inverse p() (guess x such that p(x) = y)
def _guessQ(y):
    l = -3.; r = 3.
    eps = 1e-2
    while r-l>eps:
        x = (l+r)/2.
        if p(x)<y: r = x
        else:      l = x
    x = (l+r)/2.
    return x
# NB1: p() is trivial to diff., Newton's method is also an option.
# NB2: 6y = log((exp(3-x)+1)/(exp(-3-x)+1)) can easily be inversed to
#       x = log((exp(6y-3)-exp(3))/(1-exp(6y)))
guessQ = lambda y:    \
     3. if y==0. else \
    -3. if y==1. else \
    max(-3., min(log((exp(6.*y-3.)-exp(3.))/(1.-exp(6.*y))), 3.))

def main():
    T = int(input())
    P = int(input())
    for t in range(1, T+1):
        A = [input().strip() for _ in range(_N)]
        # approximate difficulty of questions
        Q = []
        for q in range(_Q):
            o = 0
            for i in range(_N):
                if A[i][q]=='1':
                    o += 1
            Q.append(guessQ(o/_N))
        # for each player, compute the average difficulty of questions
        # answered correctly ("easy") and incorrectly ("hard")
        S = []
        for i in range(_N):
            q0 = c0 = q1 = c1 = 0
            for q in range(_Q):
                if A[i][q]=='0':
                    q0 += Q[q]
                    c0 += 1
                else:
                    q1 += Q[q]
                    c1 += 1
            # gap between "hard" and "easy" questions for that player
            S.append(q0/c0 - q1/c1)
        # select the player with the smallest gap
        # experimentally, this seems to have a >98% success rate!
        res = min(range(_N), key=(lambda i: S[i]))
        print(f'Case #{t}: {res+1}')

main()
