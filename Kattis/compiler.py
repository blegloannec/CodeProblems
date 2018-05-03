#!/usr/bin/env python3

# Using base 3 (and computing with Horner) leads to hardly reducible programs
# with up to 45 instructions (on large inputs). Almost, but not good enough...

# To reach at most 40 instructions, searching for an efficient way through
# a BFS or Dijkstra seems unavoidable (it is the intended solution).

# NB: there is no "direct" efficient approach, this is a harder variant of
# the shortest addiction-chain problem (known to be hard and not solvable
# through DP, usually studied in the context of optimal exponentiation).
# https://en.wikipedia.org/wiki/Addition-chain_exponentiation

from collections import deque

def bfs(N=256):
    R = ['X','Y']
    Q = deque()
    s0 = (0,1,1)
    Pred = {s0:None}
    Prog = {s0:('ZE X','ST Y','PH Y')}
    State = [None]*N
    Cpt = 0
    Q.append(s0)
    while Q and Cpt<N:
        s = Q.popleft()
        x = s[2]
        if State[x]==None:
            State[x] = s
            Cpt += 1
        for i in range(2):  # PH i, AD
            if s[2]+s[i]<N:
                t = (s[0],s[1],s[2]+s[i])
                if t not in Pred:
                    Pred[t] = s
                    Prog[t] = ('PH '+R[i],'AD')
                    Q.append(t)
        for i in range(2):  # PL, PH
            t = (s[2],s[1],s[2]) if i==0 else (s[0],s[2],s[2])
            if t not in Pred:
                Pred[t] = s
                Prog[t] = ('PL '+R[i],'PH '+R[i])
                Q.append(t)
    return State,Pred,Prog

def backprog(Pred,Prog,s):
    P = []
    while s!=None:
        P += list(reversed(Prog[s]))
        s = Pred[s]
    P = P[::-1] + ['PL A','DI A']
    return P

def simu(P):
    R = {'A':42, 'X':110, 'Y':54}
    S = []
    for I in P:
        C = I.split()
        if len(C)==1: # AD
            S.append((S.pop()+S.pop())&255)
        else:
            c,r = C
            if c=='PH':
                S.append(R[r])
            elif c=='PL':
                R[r] = S.pop()
            elif c=='ZE':
                R[r] = 0
            elif c=='ST':
                R[r] = 1
            else: # DI
                return R[r]

def main():
    N = int(input())
    if N==0:
        print('\n'.join(['ZE A','DI A']))
    else:
        State,Pred,Prog = bfs()
        P = backprog(Pred,Prog,State[N])
        print('\n'.join(P))

main()
