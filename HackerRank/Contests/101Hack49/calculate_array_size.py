#!/usr/bin/env python3

def main():
    n = int(input())
    D = list(map(int,input().split()))
    res = 1
    for d in D:
        res *= d
    print((res*4)//1024)

main()
