#!/usr/bin/env python3

def main():
    M = list(map(int, input()))
    X = 0
    for i in range(1,16):
        if M[i]:
            X ^= i
    if X:
        M[X] ^= 1
        if sum(M)&1:
            print('TWO ERRORS')
            return
    print(''.join(map(str, M)))

main()
