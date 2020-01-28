#!/usr/bin/env python3

def greedy(I):
    I.sort(key=(lambda lr: lr[1]))
    cnt = l0 = r0 = 0
    # r0 is the current rightmost end of a selected interval
    # l0 is the leftmost position such that [l0..r0] is covered
    # by at most 1 selected interval a each position
    for l,r in I:
        if r0<l:
            # [l0...r0]...[l...r]
            r0 = r
            cnt += 1
        elif l>=l0:
            # [l0.........r0]
            #          [l......r]
            l0,r0 = r0+1,r
            cnt += 1
    return cnt

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        I = [tuple(map(int,input().split())) for _ in range(N)]
        print(greedy(I))

main()
