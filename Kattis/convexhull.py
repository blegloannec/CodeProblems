#!/usr/bin/env python3

def left_turn(a,b,c):
    return (a[0]-c[0])*(b[1]-c[1]) - (a[1]-c[1])*(b[0]-c[0]) > 0

def andrew(S):
    S.sort()
    top = []
    bot = []
    for p in S:
        while len(top)>=2 and not left_turn(p,top[-1],top[-2]):
            top.pop()
        top.append(p)
        while len(bot)>=2 and not left_turn(bot[-2],bot[-1],p):
            bot.pop()
        bot.append(p)
    return bot[:-1]+top[:0:-1]

def main():
    while True:
        N = int(input())
        if N<=0:
            break
        P = list(set(tuple(map(int,input().split())) for _ in range(N)))
        if len(P)<=2:
            H = P
        else:
            H = andrew(P)
        print(len(H))
        for p in H:
            print(*p)

main()
