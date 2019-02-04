#!/usr/bin/env python3

from heapq import *

N = int(input())
BuyBook = {}
SellBook = {}
trade = False
for t in range(N):
    symb, order, qty, price = input().split()
    qty = int(qty)
    price = float(price)
    if symb not in BuyBook:
        BuyBook[symb] = []
        SellBook[symb] = []
    if order=='BUY':
        heappush(BuyBook[symb], (-price, t, qty))
    else:
        heappush(SellBook[symb], (price, t, qty))
    while BuyBook[symb] and SellBook[symb] and -BuyBook[symb][0][0]>=SellBook[symb][0][0]:
        buy_price, buy_t, buy_qty = heappop(BuyBook[symb])
        buy_price = -buy_price
        sell_price, sell_t, sell_qty = heappop(SellBook[symb])
        price = buy_price if buy_t<sell_t else sell_price
        qty = min(buy_qty,sell_qty)
        print('%s %d %.2f' % (symb,qty,price))
        if buy_qty>qty:
            heappush(BuyBook[symb], (-buy_price, buy_t, buy_qty-qty))
        if sell_qty>qty:
            heappush(SellBook[symb], (sell_price, sell_t, sell_qty-qty))
        trade = True
if not trade:
    print('NO TRADE')
