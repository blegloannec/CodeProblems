#!/usr/bin/env python3

# Waiting lists are useless. If two items are given to machine 1,
# then the total waiting time of the second item is max(P).
# But then it is equivalent to insert this item into machine 1 after
# that delay and ensures that it never waits in any waiting list.

_,P = map(int, input().split())
T = list(map(int, input().split()))
time = sum(T)
wait = max(T)
print(time + wait*(P-1))
