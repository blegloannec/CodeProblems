#!/usr/bin/env python3

# We use F = 119 + 23 + 5 + 1 = 148 queries.
# The first 119 are used to request the 1st letter of each permutation.
# The missing letter only appears 23 times (24 for the 4 others).
# We then request the 2nd letter of each of the 23 remaining permutations.
# The missing letter only appears 5 times (6 for the 3 others).
# We then request the 3rd letter of each of the 5 remaining permutations.
# The missing letter only appears once (2 for the 2 others).
# We finally request the 4th letter of the last remaining permutation.
# This gives us the 5th letter of the solution and we deduce the 4th.

import sys
from collections import defaultdict

def send_recv(S):
    print(S)
    sys.stdout.flush()
    return input()

def case():
    Sol = [None]*5
    Rem = list(range(119))
    for t in range(3):
        A = defaultdict(list)
        for i in Rem:
            A[send_recv(1 + 5*i+t)].append(i)
        Sol[t] = next(c for c in A if len(A[c])==len(Rem)//(5-t))
        Rem = A[Sol[t]]
    Sol[4] = send_recv(1 + 5*Rem[0]+3)
    Sol[3] = next(c for c in 'ABCDE' if c not in Sol)
    Sol = ''.join(Sol)
    assert send_recv(Sol)=='Y'

if __name__=='__main__':
    T,_ = map(int,input().split())
    for _ in range(T):
        case()
