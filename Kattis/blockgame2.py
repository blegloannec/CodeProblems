#!/usr/bin/env python3

from decimal import Decimal

# cf PE 325 & Wythoff's game

phi = (1+Decimal(5).sqrt())/2

def win(a,b):
    if a<b:
        a,b = b,a
    return a==b or phi*b<a

a,b = map(int,input().split())
print('win' if win(a,b) else 'lose')
