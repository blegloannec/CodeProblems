#!/usr/bin/env python3

def digsum(n):
    s = 0
    while n>0:
        s += n%10
        n //= 10
    return s

def main():
    n = int(input())
    Sol = []
    for d in range(min(n-1,9*9),0,-1):
        if digsum(n-d)==d:
            Sol.append(n-d)
    print(len(Sol))
    for x in Sol:
        print(x)

main()
