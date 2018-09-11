#!/usr/bin/env python3

# for the record, hard testcases generator for brackets_ultimate

import random
random.seed()

B = [['(','[','{','<'],[')',']','}','>']]

def gen(n):
    if n<0:
        return []
    n -= 1
    b = random.randint(0,3)
    res = [B[random.randint(0,1)][b]]
    while n:
        m = random.randint(1,n)
        res += gen(m)
        n -= m
    res.append(B[random.randint(0,1)][b])
    return res

def main():
    N = 10
    print(N)
    for _ in range(N):
        print(''.join(gen(random.randint(100,500))))

main()
