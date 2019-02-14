#!/usr/bin/env python3

Rounds = int(input())
Cash = int(input())
for _ in range(Rounds):
    bet = (Cash+3)//4
    Cash -= bet
    move = input().split()
    ball = int(move[0])
    if move[1]=='PLAIN':
        if ball==int(move[2]):
            Cash += 36*bet
    elif ball!=0 and ball%2==int(move[1]=='ODD'):
        Cash += 2*bet
print(Cash)
