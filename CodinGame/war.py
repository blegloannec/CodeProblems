#!/usr/bin/env python3

from collections import deque

V = {'J':11,'Q':12,'K':13,'A':14}
def val(c):
    c = c[:-1]
    return int(c) if '0'<=c[0]<='9' else V[c]

def game(C1,C2):
    W1,W2 = deque(),deque()
    step = 0
    war = False
    while C1 and C2:
        if war:
            if len(C1)<4 or len(C2)<4:
                return 0,step
            draw = 4
        else:
            step += 1
            draw = 1
        for _ in range(draw):
            W1.append(C1.popleft())
            W2.append(C2.popleft())
        v1,v2 = val(W1[-1]),val(W2[-1])
        if v1!=v2:
            C = C1 if v1>v2 else C2
            while W1:
                C.append(W1.popleft())
            while W2:
                C.append(W2.popleft())
            war = False
        else:
            war = True
    return (1 if C1 else 2),step

def main():
    N = int(input())
    C1 = deque(input() for _ in range(N))
    M = int(input())
    C2 = deque(input() for _ in range(M))
    win,step = game(C1,C2)
    if win==0:
        print('PAT')
    else:
        print(win,step)

main()
