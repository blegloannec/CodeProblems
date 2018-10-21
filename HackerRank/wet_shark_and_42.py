#!/usr/bin/env python3

# chaque bloc de 42 cases (partant de 0) coute 20 unites
#  id    0 1 2 3 4 5 ... 40 41
#  cost  0 0 1 0 1 0      1  0
# donc pour S = 20q + r
# on s'arrete sur la case 42q - 2  si r = 0 (case 40 du dernier bloc)
#                         42q + 2r sinon

P = 10**9+7

def steps(S):
    q,r = divmod(S,20)
    return 42*q + (-2 if r==0 else 2*r)

def main():
    T = int(input())
    for _ in range(T):
        S = int(input())
        print(steps(S) % P)

main()
