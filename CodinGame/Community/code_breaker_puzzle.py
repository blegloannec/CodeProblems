#!/usr/bin/env python3

from math import gcd

Alph = input()
L = len(Alph)

def encrypt(A,B, mess):
    return ''.join(Alph[((Alph.index(c)+A)*B)%L] for c in mess)

def decrypt(A,B, ciph):
    Binv = pow(B, -1, L)
    return ''.join(Alph[(Alph.index(c)*Binv-A)%L] for c in ciph)

def main():
    ciph = input()
    word = input()
    for B in range(L):
        if gcd(B,L)==1:
            for A in range(L):
                if encrypt(A,B, word) in ciph:
                    print(decrypt(A,B, ciph))
                    return

main()
