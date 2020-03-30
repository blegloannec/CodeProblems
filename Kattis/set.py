#!/usr/bin/env python3

from itertools import combinations

def main():
    C = []
    for i in range(4):
        for j,c in enumerate(input().split()):
            C.append((i*3+j+1,c))
    O = []
    for X in combinations(C,3):
        if all(len(set(X[i][1][k] for i in range(3)))!=2 for k in range(4)):
            O.append(tuple(X[i][0] for i in range(3)))
    if O:
        for X in O:
            print(*X)
    else:
        print('no sets')

main()
