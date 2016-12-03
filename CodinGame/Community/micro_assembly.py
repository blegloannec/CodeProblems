#!/usr/bin/env python3

import sys

def is_reg(s):
    return (len(s)==1 and ord('a')<=ord(s)<=ord('d'))

def reg_i(s):
    return ord(s)-ord('a')

def simu(P):
    i = 0
    while 0<=i<len(P):
        I = P[i]
        if I[0]=='MOV':
            R[reg_i(I[1])] = R[reg_i(I[2])] if is_reg(I[2]) else int(I[2])
            i += 1
        elif I[0]=='ADD':
            v1 = R[reg_i(I[2])] if is_reg(I[2]) else int(I[2])
            v2 = R[reg_i(I[3])] if is_reg(I[3]) else int(I[3])
            R[reg_i(I[1])] = v1+v2
            i += 1
        elif I[0]=='SUB':
            v1 = R[reg_i(I[2])] if is_reg(I[2]) else int(I[2])
            v2 = R[reg_i(I[3])] if is_reg(I[3]) else int(I[3])
            R[reg_i(I[1])] = v1-v2
            i += 1
        else: # JNE
            if R[reg_i(I[2])]!=(R[reg_i(I[3])] if is_reg(I[3]) else int(I[3])):
                i = int(I[1])
            else:
                i += 1

def main():
    global R
    R = list(map(int,sys.stdin.readline().split()))
    n = int(sys.stdin.readline())
    P = []
    for _ in range(n):
        P.append(sys.stdin.readline().split())
    simu(P)
    print(' '.join(map(str,R)))

main()
