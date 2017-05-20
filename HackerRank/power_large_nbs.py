#!/usr/bin/env python3

def main():
    P = 10**9+7  # prime
    PhiP = P-1   # euler phi(P)
    T = int(input())
    for _ in range(T):
        A,B = input().split()
        AmodP = 0
        for c in A:
            AmodP = (10*AmodP + ord(c)-ord('0')) % P
        BmodPhiP = 0
        for c in B:
            BmodPhiP = (10*BmodPhiP + ord(c)-ord('0')) % PhiP
        print(pow(AmodP,BmodPhiP,P))

main()
