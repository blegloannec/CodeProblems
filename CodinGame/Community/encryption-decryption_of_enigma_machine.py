#!/usr/bin/env python3

# rien a voir avec Enigma au final...

def c2i(c):
    return ord(c)-ord('A')

def i2c(i):
    return chr(i+ord('A'))

def encrypt(d,R,M):
    return ''.join(i2c(R[2][R[1][R[0][(c2i(c)+d+i)%26]]]) for i,c in enumerate(M))

def inverse(P):
    I = [0]*26
    for i in range(26):
        I[P[i]] = i
    return I

def decrypt(d,R,C):
    I = [inverse(P) for P in R]
    return ''.join(i2c((I[0][I[1][I[2][c2i(c)]]]-d-i)%26) for i,c in enumerate(C))

def main():
    op = input()
    d = int(input())
    R = [[c2i(c) for c in input()] for _ in range(3)]
    M = input()
    print(encrypt(d,R,M) if op=='ENCODE' else decrypt(d,R,M))

main()
