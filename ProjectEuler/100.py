#!/usr/bin/env python

# b*(b-1) / n*(n-1) = 1/2
# x(x-1) = (x-1/2)^2 - 1/4
# 2(b-1/2)^2 - 1/2 = (n-1/2)^2 - 1/4
# -1 = (2n-1)^2 - 2(2b-1)^2
# N = 2n-1, B = 2b-1
# N^2 - 2B^2 = -1
# Negative (due to -1) Pell equation with D = 2
# https://en.wikipedia.org/wiki/Pell%27s_equation
# see also pb 66 & 94
# Not always solvable in general, but has solutions for D = 2

def main():
    # easily found fundamental solution
    x0,y0 = 1,1
    x,y = x0,y0
    while True:
        x,y = x0*x + 2*y0*y, x0*y + y0*x
        if x%2==1 and y%2==1 and (x+1)/2>10**12:
            print (y+1)/2
            break

main()
