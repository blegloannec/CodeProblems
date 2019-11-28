#!/usr/bin/env python3

def precomp(N=31):
    T = [0]*N
    T[0] = S = 1
    for i in range(2,N,2):
        # ==   ||   ==   ====...==
        # ==   ||   ||   |==...==|
        # ==   ==   ||   |==...==|
        T[i] = T[i-2] + 2*S
        S += T[i]
    return T

def main():
    T = precomp()
    while True:
        n = int(input())
        if n<0:
            break
        print(T[n])

main()
