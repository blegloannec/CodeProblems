#!/usr/bin/env python3

## Fastest mode?
# Several possible implementations. A really too clumsy one might time out
# but no tricks are required. The following is a possible / reasonable /
# expectable solution.

from collections import deque

Rule = [[1,2],[0],[0,0,0]]
Zero = [0,1,3]

N = int(input())
print(N)

Q = deque([0]*N)
while len(Q)>1:
    x = Q.popleft()
    y = Q.popleft()
    Q += Rule[x]
    N += Zero[x] - (x==0) - (y==0)
    if len(Q)==N:
        print(N)

## Shortest mode?
# Compact implementations are an option. Or analyze what the birds do
# and deduce a formula (which should be even shorter). Or guess that
# formula empirically (as one would do in reverse mode).

## No reverse mode?
# Would be possible, yet uninteresting, unoriginal and spoils the fun IMO.

## Who's Emilia?
# She works at the Syracuse post office. In Sicilia... unless it's NY state.
