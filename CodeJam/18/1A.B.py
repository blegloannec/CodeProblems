#!/usr/bin/env python3

def valid(T):
    BB = []
    for (M,S,P) in MSP:
        if P>T:
            BB.append(0)
        else:
            BB.append(min(M,(T-P)//S))
    BB.sort(reverse=True)
    return sum(BB[:R])>=B

def dicho():
    L,R = 0,(1<<62)
    while L<R:
        T = (L+R)//2
        if valid(T):
            R = T
        else:
            L = T+1
    return L

def main():
    global R,B,C,MSP
    T = int(input())
    for t in range(1,T+1):
        R,B,C = map(int,input().split())
        MSP = [tuple(map(int,input().split())) for _ in range(C)]
        print('Case #%d: %d' % (t,dicho()))

main()
