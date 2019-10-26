#!/usr/bin/env python3

phi = (1.+5.**0.5)/2.

def main():
    T = int(input())
    for _ in range(T):
        U = int(input())
        res = (U-1,1)
        # turns out the optimal to climb backwards from U
        # is U / golden ratio
        x = int(U/phi)
        for U0 in (x,x+1):
            u0,u1 = U0,U
            while u1>=u0>0:
                res = min((u1,u0), res)
                u0,u1 = u1-u0,u0
        print(res[1],res[0])

main()
