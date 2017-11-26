#!/usr/bin/env python3

def trigoturn(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1])-(a[1]-c[1])*(b[0]-c[0])>0

def andrew(S):
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top)>=2 and not trigoturn(p,top[-1],top[-2]):
            top.pop()
        top.append(p)
        while len(bot)>= 2 and not trigoturn(bot[-2],bot[-1],p):
            bot.pop()
        bot.append(p)
    return bot[:-1]+top[:0:-1]

def main():
    K = int(input())
    print(K)
    for k in range(K):
        if k>0:
            input()  # -1
            print(-1)
        N = int(input())
        S = []
        for _ in range(N):
            x,y = map(int,input().split())
            S.append((y,x))
        H = andrew(S)
        i = S.index(min(S))
        H = H[i:]+H[:i]
        H.append(H[0])
        print(len(H))
        for y,x in reversed(H):
            print(x,y)

main()
