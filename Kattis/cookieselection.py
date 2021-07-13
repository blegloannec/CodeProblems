#!/usr/bin/env python3

from heapq import *
import sys

# classical online median

def main():
    Bot = []
    Top = []
    for L in sys.stdin.readlines():
        if L[0]=='#':
            assert Top
            sys.stdout.write(f'{heappop(Top)}\n')
        else:
            d = int(L)
            if not Top or Top[0]<=d:
                heappush(Top, d)
            else:
                heappush(Bot, -d)
        while len(Top)-len(Bot)>1:
            heappush(Bot, -heappop(Top))
        while len(Bot)>len(Top):
            heappush(Top, -heappop(Bot))

main()
