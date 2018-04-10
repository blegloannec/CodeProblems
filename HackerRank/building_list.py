#!/usr/bin/env python3

def lexsub(S,C,i=0):
    for j in range(i,len(S)):
        C.append(S[j])
        yield ''.join(C)
        yield from lexsub(S,C,j+1)
        C.pop()

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        for C in lexsub(S,[]):
            print(C)

main()
