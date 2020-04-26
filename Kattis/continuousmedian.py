#!/usr/bin/env python3

import sys
from heapq import *

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        S = 0
        TopHalf = []
        BotHalf = []
        for i,a in enumerate(A):
            if not TopHalf or TopHalf[0]<=a:
                heappush(TopHalf, a)
            else:
                heappush(BotHalf, -a)
            if len(TopHalf)>len(BotHalf)+1:
                heappush(BotHalf, -heappop(TopHalf))
            elif len(TopHalf)<len(BotHalf):
                heappush(TopHalf, -heappop(BotHalf))
            if i%2==0:
                S += TopHalf[0]
            else:
                S += (TopHalf[0]-BotHalf[0])//2
        sys.stdout.write(f'{S}\n')

main()
