#!/usr/bin/env python3

import sys

# when sending A, we receive sum_{d=1..6}  Rd * 2^(A//d) mod 2^63

A = 54
B = 160
MASK = 127
CA = [A//d for d in range(1,7)]
CB = [B//d for d in range(1,7)]

def send_recv(S):
    print(S)
    sys.stdout.flush()
    return int(input())

# We solve each case in 3 steps:
#  2 requests to deduce R1 & R2, then R3 & R4
#  + linear system solving of size 2 to deduce R5 and R6
# NB (from official analysis): With better requests, it was directly
#  possible to deduce R4 & R5 & R6 (from 200), then R1 & R2 & R3 (from 56)

def case():
    R = [0]*6
    # we get R1 and R2 using A = 54
    X = send_recv(A)
    R[0] =  X>>CA[0]
    R[1] = (X>>CA[1]) & MASK
    # we get R3 and R4 using B = 160
    Y = send_recv(B)
    R[2] = (Y>>CB[2]) & MASK
    R[3] = (Y>>CB[3]) & MASK
    # we remove the R1 to R4 parts from X and Y
    X -= sum(R[i]<<CA[i] for i in range(4))
    Y -= (R[2]<<CB[2]) + (R[3]<<CB[3])
    # this leaves us with 2 linear equations in R5 and R6
    DC = CB[4]-CA[4]
    R[5] = ((X<<DC) - Y) // ((1<<(CA[5]+DC)) - (1<<CB[5]))
    R[4] = (X - (R[5]<<CA[5])) >> CA[4]
    assert send_recv(' '.join(map(str,R)))==1

if __name__=='__main__':
    T,_ = map(int,input().split())
    for _ in range(T):
        case()
