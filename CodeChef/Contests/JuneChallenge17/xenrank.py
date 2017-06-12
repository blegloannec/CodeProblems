#!/usr/bin/env python3

def rank(x,y):
    return (x+y)*(x+y+1)//2 + x + 1

def main():
    T = int(input())
    for _ in range(T):
        U,V = map(int,input().split())
        print(rank(U,V))

main()
