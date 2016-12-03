#!/usr/bin/env python

from operator import mul

#Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
#Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
#Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
#Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8

I = [(3,0,0,-3,2),(-3,3,0,0,9),(-1,0,4,0,1),(0,0,-2,2,8)]
T = 100
C = 500

def main():
    maxs = 0
    for i in range(T+1):
        for j in range(T+1-i):
            for k in range(T+1-i-j):
                for l in range(T+1-i-j-k):
                    p = [0,0,0,0]
                    for a in range(4):
                        p[a] = max(0,I[0][a]*i+I[1][a]*j+I[2][a]*k+I[3][a]*l)
                    s = reduce(mul,p,1)
                    maxs = max(maxs,s)
    print maxs

def main2():
    maxs = 0
    for i in range(T+1):
        cal0 = i*I[0][4]
        if cal0>C:
            break
        for j in range(T+1-i):
            cal1 = cal0+j*I[1][4]
            if cal1>C:
                break
            for k in range(T+1-i-j):
                cal2 = cal1+k*I[2][4]
                if cal2>C:
                    break
                for l in range(T+1-i-j-k):
                    cal3 = cal2+l*I[3][4]
                    if cal3>C:
                        break
                    if cal3<C:
                        continue
                    p = [0,0,0,0]
                    for a in range(4):
                        p[a] = max(0,I[0][a]*i+I[1][a]*j+I[2][a]*k+I[3][a]*l)
                    s = reduce(mul,p,1)
                    maxs = max(maxs,s)
    print maxs

main2()
