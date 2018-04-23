#!/usr/bin/env python3

def main():
    n = int(input())
    x = 0
    for _ in range(n):
        c,y = input().split()
        y = int(y)
        if c=='add' and y>0:
            x += y
        elif c=='set' and y>x:
            x = y
    print(x)

main()
