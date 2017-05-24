#!/usr/bin/env python3

D = {'H':1,'.':0,'T':-1}

def main():
    R = int(input())
    for _ in range(R):
        L = int(input())
        P = input()
        x = 0
        for c in P:
            x += D[c]
            if not 0<=x<=1:
                break
        print('Valid' if x==0 else 'Invalid')

main()
