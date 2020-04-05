#!/usr/bin/env python3

def sol(X,Y):
    N = 1
    A = abs(X)+abs(Y)
    while N*(N+1)<2*A or A%2!=((N*(N+1))//2)%2:
        N += 1
    S = []
    for n in range(N,0,-1):
        if abs(X)>=abs(Y):
            if X>0:
                X -= n
                S.append('E')
            else:
                X += n
                S.append('W')
        else:
            if Y>0:
                Y -= n
                S.append('N')
            else:
                Y += n
                S.append('S')
    #assert(X==Y==0)
    return ''.join(reversed(S))

def main():
    T = int(input())
    for t in range(1,T+1):
        X,Y = map(int,input().split())
        print('Case #%d: %s' % (t,sol(X,Y)))

main()
