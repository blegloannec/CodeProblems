#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1, T+1):
        N,K = map(int, input().split())
        P = sorted(map(int, input().split()))
        One = [P[0]-1, K-P[-1]]
        Two = [0]
        for i in range(1, len(P)):
            # interval size
            d = P[i]-P[i-1]-1
            if d>0:
                # pick one end of the interval
                One.append((d+1)//2)
                # pick both ends
                Two.append(d)
        One.sort()
        cov = max(One[-1]+One[-2], max(Two))
        print(f'Case #{t}: {cov/K}')

main()
