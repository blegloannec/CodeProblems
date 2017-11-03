#!/usr/bin/env python3

R = ["0123456789","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","!@#$%^&*()-+"]

def strong(s):
    d0 = max(0,6-len(s))
    d1 = sum(int(not any(c in s for c in req)) for req in R)
    return max(d0,d1)

def main():
    n = int(input())
    s = input()
    print(strong(s))

main()
