#!/usr/bin/env python3

import sys
input = sys.stdin.readline

# max of ax² + bx + c over [x₀, x₁]
def max_parabola(a,b,c, x0,x1):
    y = max(a*x0*x0+b*x0+c, a*x1*x1+b*x1+c)
    if a<0:
        # derivative 2ax + b
        x = -b / 2. / a
        if x0 <= x <= x1:
            y = max(y, a*x*x+b*x+c)
    return y

def main():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    P.append((0,0,0,0))  # sentinel
    P.sort(key=(lambda abct: abct[3]))
    T = 100000
    A = B = C = Y = 0
    i = N
    while T>0:
        a,b,c,t = P[i]
        while t==T:
            A += a; B += b; C += c
            i -= 1
            a,b,c,t = P[i]
        Y = max(Y, max_parabola(A,B,C, t,T))
        T = t
    print(Y)

main()
