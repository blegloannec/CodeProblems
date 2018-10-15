#!/usr/bin/env python3

n = input()
form = '%0' + str(len(n)) + 'd'
trace = []
time = {}
t = 0
while n not in time:
    trace.append(n)
    time[n] = t
    t += 1
    x = ''.join(sorted(n))
    y = x[::-1]
    n = form % (int(y)-int(x))
print(*trace[time[n]:])
