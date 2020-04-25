#!/usr/bin/env python3

import sys
from heapq import *

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        Ask = []
        Bid = []
        stock = '-'
        for _ in range(N):
            order = sys.stdin.readline().split()
            qty, price = int(order[1]), int(order[-1])
            if order[0][0]=='s':
                heappush(Ask, (price, qty))
            else:
                heappush(Bid, (-price, qty))
            while Ask and Bid and Ask[0][0]<=-Bid[0][0]:
                aprice, aqty = heappop(Ask)
                stock = aprice
                bprice, bqty = heappop(Bid)
                if   aqty>bqty:
                    heappush(Ask, (aprice, aqty-bqty))
                elif aqty<bqty:
                    heappush(Bid, (bprice, bqty-aqty))
            aprice = Ask[0][0] if Ask else '-'
            bprice = -Bid[0][0] if Bid else '-'
            sys.stdout.write(f'{aprice} {bprice} {stock}\n')

main()
