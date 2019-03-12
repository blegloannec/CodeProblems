#!/usr/bin/env python3

Size = 40
Jail, GoToJail = 10, 30

def play(Pos, Dice):
    P = len(Pos)
    Jailed = [0]*P
    p = dbls = 0
    for d,e in Dice:
        if Jailed[p]>0:
            if d==e or Jailed[p]==1:
                Pos[p] = (Pos[p]+d+e) % Size
                Jailed[p] = 0
            else:
                Jailed[p] -= 1
            p = (p+1) % P
        else:
            Pos[p] = (Pos[p]+d+e) % Size
            if Pos[p]==GoToJail:
                Pos[p] = Jail
                Jailed[p] = 3
                p = (p+1) % P
                dbls = 0
            elif d!=e:
                p = (p+1) % P
                dbls = 0
            else:
                dbls += 1
                if dbls==3:
                    Pos[p] = Jail
                    Jailed[p] = 3
                    p = (p+1) % P
                    dbls = 0

if __name__=='__main__':
    P = int(input())
    Player = [None]*P
    Pos = [0]*P
    for i in range(P):
        Player[i], Pos[i] = input().split()
        Pos[i] = int(Pos[i])
    D = int(input())
    Dice = [tuple(map(int,input().split())) for _ in range(D)]
    play(Pos, Dice)
    for player,pos in zip(Player,Pos):
        print(player, pos)
