#!/usr/bin/env python3

N = int(input())
Player = [input() for _ in range(N)]
min_rounds = float('inf')
for i in range(N):
    Shots = input().split()
    score = prev_score = rounds = shots_cnt = 0
    for s in Shots:
        if shots_cnt==0:                 # new round
            rounds += 1
            miss_cnt = 0
            prev_score = score
        shots_cnt = (shots_cnt+1)%3
        if s=='X':                       # miss
            score = max(0,score-20)
            miss_cnt += 1
            if miss_cnt==2:
                score = max(0,score-10)
            elif miss_cnt==3:
                score = 0
        else:                            # hit
            score += eval(s)
            miss_cnt = 0
            if score==101:
                break
            if score>101:
                shots_cnt = 0
                score = prev_score
    if score==101 and rounds<min_rounds:
        min_rounds,winner = rounds,Player[i]
print(winner)
