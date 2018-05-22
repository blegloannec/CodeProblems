#!/usr/bin/env python3

def digsum(n):
    s = 0
    while n>0:
        n,c = divmod(n,10)
        s += c
    return s

def meeting(r1,r2):
    while r1!=r2:
        if r1<r2:
            r1 += digsum(r1)
        else:
            r2 += digsum(r2)
    return r1

def main():
    r1 = int(input())
    r2 = int(input())    
    print(meeting(r1,r2))

main()
