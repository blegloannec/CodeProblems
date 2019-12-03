#!/usr/bin/env python3

Decimals = {}
Rate = {}

def price_doll(price):
    price, currency = price[:-4].replace(' ',''), price[-3:]
    try:
        dot = next(c for c in reversed(price) if not '0'<=c<='9')
        if price.count(dot)>1:
            dot = None
    except StopIteration:
        dot = None
    curr = float(''.join('.' if c==dot else c for c in price if '0'<=c<='9' or c==dot))
    doll = curr/Rate[currency]
    return doll

def floor(x, prec):
    p10 = 10**prec
    return int(x*p10)/p10

def main():
    N = int(input())
    for _ in range(N):
        code, rate, decimals = input().split()
        Rate[code] = float(rate)
        Decimals[code] = int(decimals)
    price = input()
    target = input()
    dec = Decimals[target]
    form = '%%.%df' % dec
    res = price_doll(price)*Rate[target]
    print(form % floor(res,dec))

main()
