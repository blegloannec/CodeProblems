#!/usr/bin/env python3

def avg_top(R):
    c = 0
    s = 0.
    for r in R:
        if r>=90:
            c += 1
            s += r
    return s/c

def rnd(x):
    x *= 100.
    x0 = int(x)
    if x-x0>=0.5:
        x0 += 1
    x0 /= 100.
    return x0
    
def main():
    n = int(input())
    R = [int(input()) for _ in range(n)]
    print('%.2f' % rnd(avg_top(R)))

main()
