#!/usr/bin/env python3

# We cannot change the inner order of even digits, or odd digits,
# but we can interlace them arbitrarily.

N = list(map(int, input()))
E = [d for d in reversed(N) if d&1==0]
O = [d for d in reversed(N) if d&1==1]
R = []
while E or O:
    if not O or (E and E[-1]>O[-1]):
        R.append(E.pop())
    else:
        R.append(O.pop())
print(*R, sep='')
