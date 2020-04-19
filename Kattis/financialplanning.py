#!/usr/bin/env python3

def main():
    N,M = map(int,input().split())
    I = [tuple(map(int,input().split())) for _ in range(N)]
    I.sort(key=(lambda PC: PC[1]/PC[0]))
    dmin = float('inf')
    A,B = M,0
    for p,c in I:
        A += c
        B += p
        dmin = min(dmin, (A+B-1)//B)
    print(dmin)

main()
