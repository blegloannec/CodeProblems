#!/usr/bin/env python3

def is_sqrt(n):
    return round(n**0.5)**2==n

def main():
    t = int(input())
    for _ in range(t):
        d,k = map(int,input().split())
        # x^2 + y^2 = d
        x = C = 0
        while 2*x*x<=d:
            if is_sqrt(d-x*x):
                C += 4 if x==0 or 2*x*x==d else 8
            x += 1
        print(('im' if k<C else '')+'possible')

main()
