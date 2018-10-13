#!/usr/bin/env python3

def total_dp(n,a):
    X = [{a}]
    d = 0
    while n not in X[-1]:
        d += 1
        X.append(set())
        for i in range(d):
            j = d-1-i
            for x in X[i]:
                for y in X[j]:
                    if i<=j:
                        X[d].add(x+y)
                        X[d].add(x*y)
                    X[d].add(x-y)
                    if y!=0 and x%y==0:
                        X[d].add(x//y)
    return d

N = int(input())
a = int(input())
print(total_dp(N,a)+1)
