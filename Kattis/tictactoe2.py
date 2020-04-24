#!/usr/bin/env python3

S = 3
S2 = S*S
NP,P0,P1, = '.','X','O'
idx = lambda i,j: S*i+j

def win_check(G, Win, Cells):
    c = G[Cells[0]]
    if c!='.' and all(G[i]==c for i in Cells):
        p = int(c=='O')
        for i in Cells:
            Win[p][i] += 1

def valid(G):
    # counting
    Cnt = [G.count(P0), G.count(P1)]
    if not Cnt[1]<=Cnt[0]<=Cnt[1]+1:
        return False
    plast = 1 if Cnt[0]==Cnt[1] else 0
    # winning lines
    Win = [[0]*S2, [0]*S2]
    for i in range(S):
        win_check(G, Win, tuple(idx(i,j) for j in range(S)))
    # winning colums
    for j in range(S):
        win_check(G, Win, tuple(idx(i,j) for i in range(S)))
    # winning diagonals
    win_check(G, Win, tuple(idx(i,i) for i in range(S)))
    win_check(G, Win, tuple(idx(i,2-i) for i in range(S)))
    # consistency check
    if any(Win[plast^1]) or sum(int(c>1) for c in Win[plast])>1:
        return False
    return True

def main():
    N = int(input())
    for i in range(N):
        if i>0:
            input()
        G = ''.join(input() for _ in range(S))
        print('yes' if valid(G) else 'no')

main()
