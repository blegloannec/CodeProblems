#!/usr/bin/env python3

def to_bin(c):
    n = ord(c)
    B = [0]*7
    for i in range(6,-1,-1):
        B[i] = n&1
        n >>= 1
    return B

def encode(M):
    B = []
    i = 0
    while i<len(M):
        c = M[i]
        k = 1
        i += 1
        while i<len(M) and M[i]==c:
            k += 1
            i += 1
        B.append('0'*(2-int(c)))
        B.append('0'*k)
    return ' '.join(B)

def main():
    M = []
    for c in input():
        M += to_bin(c)
    print(encode(M))

main()
