#!/usr/bin/env python3

# kinda sloppy problem, so stupid brute force...

import operator
from itertools import product
from functools import reduce

O = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}

def main():
    L,R = input().split('=')
    L,R = L.split(),int(R)
    o = L[1]
    L = L[::2]
    M,Q = [],[]
    for s in L:
        Q += [(len(M),j) for j in range(len(s)) if s[j]=='?']
        M.append(list(s))
    for P in product(range(10),repeat=len(Q)):
        for i in range(len(Q)):
            M[Q[i][0]][Q[i][1]] = str(P[i])
        if reduce(O[o],(int(''.join(s)) for s in M))==R:
            break
    print((' '+o+' ').join(''.join(s) for s in M),'=',R)

main()
