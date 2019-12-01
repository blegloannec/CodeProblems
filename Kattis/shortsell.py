#!/usr/bin/env python3

N,K = map(int,input().split())
X = [100*int(x) for x in input().split()]
max_profit = 0
min_repay_cost = float('inf')
for i in range(N-1,-1,-1):
    min_repay_cost += K
    max_profit = max(max_profit, X[i]-min_repay_cost)
    min_repay_cost = min(min_repay_cost, X[i]+K)
print(max_profit)
