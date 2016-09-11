#!/usr/bin/env python

# 4^t = 2^t + k
# x = 2^t
# x^2 - x - k = 0
# D = 1 + 4*k
# x = (1+sqrt(D))/2 > 0
# t = log2(x)
# on a une partition lorsque x est entier
# on a une partition parfaite lorsque x
# est une puissance de 2

def is_pow2(x):
    return (x>0) and not x&(x-1)

def main():
    a,b = 1,12345 # fraction limite
    part,perf = 0,0
    n = 3
    while b*perf>=a*part:
        if (n*n-1)%4==0:
            # il existe k entier pour lequel D = 1+4k = n^2
            # avec n impair, donc partition
            part += 1
            k = (n*n-1)/4
            if is_pow2(1+n):
                # 1+sqrt(D) est une puissance de 2
                # donc partition parfaite
                perf += 1
        n += 2
    print k

main()
