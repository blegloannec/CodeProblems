#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        D,N = map(int,input().split())
        tps = 0
        for _ in range(N):
            Ki,Si = map(int,input().split())
            tps = max(tps,(D-Ki)/Si)
        print('Case #%d: %f' % (t,D/tps))

main()
