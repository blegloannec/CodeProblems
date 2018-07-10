#!/usr/bin/env python3

EPS = 1e-6

def green(v,DistPer):
    return all((int(D/v+EPS)//P)%2==0 for D,P in DistPer)

def main():
    Vmax = int(input())
    N = int(input())
    DistPer = [tuple(map(int,input().split())) for _ in range(N)]
    V = next(Vkmh for Vkmh in range(Vmax,0,-1) if green(Vkmh/3.6,DistPer))
    print(V)

main()
