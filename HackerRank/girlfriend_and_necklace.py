#!/usr/bin/env python3

# /!\ "the necklace is a single string and not a loop"

S = 3
P = 10**9+7

def mult(A, B):
    C = [[0]*S for _ in range(S)]
    for i in range(S):
        for j in range(S):
            for k in range(S):
                C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % P
    return C

# The valid necklaces are the words on {R,B} without any factor BB or BRB
# Automaton RR --R--> RR
#              --B--> RB
#           RB --R--> BR
#           BR --R--> RR
A = [[1,0,1],
     [1,0,0],
     [0,1,0]]
# (Of course this could also be expressed as a recurrence.)

Apow2 = [[[1,0,0],[0,1,0],[0,0,1]], A]
for _ in range(1,62):
    Apow2.append(mult(Apow2[-1],Apow2[-1]))

def Apow(b):
    result = [[1,0,0],[0,1,0],[0,0,1]]
    p2 = 1
    while b:
        if b&1:
            result = mult(result, Apow2[p2])
        p2 += 1
        b >>= 1
    return result

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        M = Apow(N-2)
        cnt = 0
        for i in range(3):
            for j in range(3):
                cnt = (cnt + M[i][j]) % P
        print(cnt)

main()
