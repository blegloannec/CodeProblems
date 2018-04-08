#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        V = list(map(int,input().split()))
        W = [sorted(V[::2]),sorted(V[1::2])]
        res = None
        for i in range(N-1):
            if W[i%2][i//2]>W[(i+1)%2][(i+1)//2]:
                res = i
                break
        if res==None:
            print('Case #%d: OK' % t)
        else:
            print('Case #%d: %d' % (t,res))

main()
