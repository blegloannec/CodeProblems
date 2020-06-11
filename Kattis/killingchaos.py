#!/usr/bin/env python3

import sys
input = sys.stdin.readline

rnd10 = lambda s: (s+9)//10

def find(x):
    if Repr[x] is None:
        return x
    Repr[x] = find(Repr[x])
    return Repr[x]

def union(x, y):
    global chaos_sum, seg_cnt
    x0 = find(x)
    y0 = find(y)
    if x0!=y0:
        chaos_sum -= rnd10(Size[x0]) + rnd10(Size[y0])
        Repr[y0] = x0
        Size[x0] += Size[y0]
        chaos_sum += rnd10(Size[x0])
        seg_cnt -= 1

def main():
    global Repr, Size, chaos_sum, seg_cnt
    N = int(input())
    Size = list(map(int, input().split()))
    O = list(map(int, input().split()))
    Active = [False]*N
    Repr = [None]*N
    max_chaos = chaos_sum = seg_cnt = 0
    for i in reversed(O):
        i -= 1
        Active[i] = True
        chaos_sum += rnd10(Size[i])
        seg_cnt += 1
        if i>0 and Active[i-1]:
            union(i-1, i)
        if i+1<N and Active[i+1]:
            union(i, i+1)
        max_chaos = max(max_chaos, chaos_sum*seg_cnt)
    print(10*max_chaos)

main()
