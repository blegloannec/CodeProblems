#!/usr/bin/env python3

And = {('0','0'): '0', ('0','1'): '0', ('0','?'): '0',
       ('1','0'): '0', ('1','1'): '1', ('1','?'): '?',
       ('?','0'): '0', ('?','1'): '?', ('?','?'): '?'}

Or  = {('0','0'): '0', ('0','1'): '1', ('0','?'): '?',
       ('1','0'): '1', ('1','1'): '1', ('1','?'): '1',
       ('?','0'): '?', ('?','1'): '1', ('?','?'): '?'}

def simu(P):
    B = ['?']*32
    for I in P:
        if I[0]=='CLEAR':
            i = int(I[1])
            B[i] = '0'
        elif I[0]=='SET':
            i = int(I[1])
            B[i] = '1'
        elif I[0]=='OR':
            i,j = int(I[1]),int(I[2])
            B[i] = Or[B[i],B[j]]
        else: # AND
            i,j = int(I[1]),int(I[2])
            B[i] = And[B[i],B[j]]
    return ''.join(reversed(B))

def main():
    while True:
        N = int(input())
        if N<=0:
            break
        P = [input().split() for _ in range(N)]
        print(simu(P))

main()
