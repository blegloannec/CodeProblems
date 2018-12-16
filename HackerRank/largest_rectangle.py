#!/usr/bin/env python3

def hist_max_rect(H):
    H.append(0)
    S = []
    res = 0
    for i in range(len(H)):
        x = i
        while S and H[i]<=S[-1][1]:
            x,h = S.pop()
            # an interval of height h starts at x and ends at i-1
            res = max(res,h*(i-x))
        S.append((x,H[i])) # an interval of height H[i] starts from x
    return res

def main():
    N = int(input())
    H = list(map(int,input().split()))
    print(hist_max_rect(H))

main()
