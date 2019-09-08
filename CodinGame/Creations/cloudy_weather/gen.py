#!/usr/bin/env python3

import sys, random
random.seed()

def random_point(S, Rects):
    a,b = random.randint(0,S),random.randint(0,S)
    while any(x<=a<x+w and y<=b<y+h for x,y,w,h in Rects):
        a,b = random.randint(0,S),random.randint(0,S)
    return a,b

dist = lambda A,B: abs(A[0]-B[0]) + abs(A[1]-B[1])

def gen_random(seed, size, cloud_cnt, cloud_size=None):
    random.seed(seed)
    if cloud_size is None:
        cloud_size = size//8
    Clouds = []
    for _ in range(cloud_cnt):
        x, y = random.randint(1,size), random.randint(1,size)
        w, h = random.randint(1,cloud_size), random.randint(1,cloud_size)
        Clouds.append((x,y,w,h))
    P0, P1 = random_point(size, Clouds), random_point(size, Clouds)
    while dist(P0,P1)<=size:
        P0, P1 = random_point(size, Clouds), random_point(size, Clouds)
    print(*P0)
    print(*P1)
    print(cloud_cnt)
    for C in Clouds:
        print(*C)

if __name__=='__main__':
    seed = random.randint(0,1<<30)
    print(seed, file=sys.stderr)
    # very small map 2
    gen_random(seed, 10, 4, 7)
    #gen_random(seed, 15, 5, 10)
    # small map 3
    #gen_random(seed, 100, 40, 35)
    # medium map 2
    #gen_random(seed, 800, 50, 250)
    #gen_random(seed, 800, 100, 150)
    # large map 4
    #gen_random(seed, 10**9, 150)
    #gen_random(seed, 10**9, 200, 10**9//6)
    #gen_random(seed, 10**9, 250)
