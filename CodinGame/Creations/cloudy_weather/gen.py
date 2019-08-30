#!/usr/bin/env python3

import random
random.seed()

def random_point(S, Rects):
    a,b = random.randint(0,S),random.randint(0,S)
    while any(x<=a<x+w and y<=b<y+h for x,y,w,h in Rects):
        a,b = random.randint(0,S),random.randint(0,S)
    return a,b

dist = lambda A,B: abs(A[0]-B[0]) + abs(A[1]-B[1])

def gen_random(S, N):
    s = S//8
    Clouds = []
    for _ in range(N):
        x = random.randint(0,S)
        y = random.randint(0,S)
        w = random.randint(1,s)
        h = random.randint(1,s)
        Clouds.append((x,y,w,h))
    P0, P1 = random_point(S, Clouds), random_point(S, Clouds)
    while dist(P0,P1)<=S:
        P0, P1 = random_point(S, Clouds), random_point(S, Clouds)
    print(*P0)
    print(*P1)
    print(N)
    for C in Clouds:
        print(*C)

gen_random(500, 200)
