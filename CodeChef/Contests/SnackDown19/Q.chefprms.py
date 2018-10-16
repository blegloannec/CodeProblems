#!/usr/bin/env python3

M = 200
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def gen_sp(P):
    SP = []
    for i in range(len(P)):
        for j in range(i+1,len(P)):
            sp = P[i]*P[j]
            if sp>M:
                continue
            SP.append(sp)
    SP.sort()
    return SP

def gen_sum_sp(SP):
    SSP = set()
    for i in range(len(SP)):
        for j in range(i,len(SP)):
            ssp = SP[i]+SP[j]
            if ssp>M:
                continue
            SSP.add(ssp)
    return SSP

def main():
    SP = gen_sp(P)
    SSP = gen_sum_sp(SP)
    T = int(input())
    for _ in range(T):
        N = int(input())
        print('YES' if N in SSP else 'NO')

main()
