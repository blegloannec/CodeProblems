#!/usr/bin/env python3

from datetime import datetime, timedelta

F = '%I:%M:%S %p'

to = datetime.strptime(input(), F)
t0 = datetime.strptime('8:00:00 AM', F)
dt = to - t0
if to < t0:
    dt += timedelta(days=1)

assert dt.total_seconds() % (4*60-1) == 0

dt = dt / timedelta(seconds=4*60-1) * timedelta(seconds=4*60)
tt = t0 + dt
print(tt.strftime(F).lstrip('0'))
