#!/usr/bin/env python3

def f(b,x):
    return int(2.**(b-x*x))*(1e-9)

def main():
    u,b = map(float,input().split())
    for _ in range(200):
        u = f(b,u)
    print(u+f(b,u))

main()
