#!/usr/bin/env python3

E0 = 1.

def E(n,t):
    if n==0:
        return E0
    e1 = E(n-1,t)
    # assume we get proba t <= p <= 1
    # 2*e1*p > 1 <=> p > 1/(2*e1)
    t0 = max(t, 1./(2.*e1))
    # q = proba to get p > 1/(2*e1)
    q = (1.-t0)/(1.-t)
    e = (1.-q)*E0 + q*e1*(1.+t0)
    return e

def main():
    while True:
        n,t = input().split()
        n,t = int(n), float(t)
        if n==0:
            break
        print('%.3f' % E(n,t))

main()
