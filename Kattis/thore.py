#!/usr/bin/env python3

def main():
    N = int(input())
    SB = [input() for _ in range(N)]
    TH = 'ThoreHusfeldt'
    if TH==SB[0]:
        print('Thore is awesome')
        return
    jmax = -1
    for X in SB:
        j = 0
        while j<len(X) and j<len(TH) and X[j]==TH[j]:
            j += 1
        if j==len(TH)==len(X):
            print(TH[:jmax+1])
            return
        if j>=len(TH)-1:
            print('Thore sucks')
            return
        jmax = max(jmax, j)

main()
