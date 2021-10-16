#!/usr/bin/env python3

def is_at_pos(i0,j0):
    for i in range(wh):
        for j in range(ww):
            if W[i][j]!=' ' and P[i0+i][j0+j]!=W[i][j]:
                return False
    return True

def main():
    global ww,wh,W, P
    ww,wh = map(int, input().split())
    W = [input() for _ in range(wh)]
    pw,ph = map(int, input().split())
    P = [input() for _ in range(ph)]
    for i0 in range(ph-wh+1):
        for j0 in range(pw-ww+1):
            if is_at_pos(i0,j0):
                print(j0,i0)
                return

main()
