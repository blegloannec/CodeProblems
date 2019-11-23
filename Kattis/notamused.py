#!/usr/bin/env python3

import sys
from collections import defaultdict

day = 0
for L in sys.stdin.readlines():
    L = L.split()
    if L[0]=='OPEN':
        day += 1
        Tin = defaultdict(int)
        Bill = defaultdict(int)
    elif L[0]=='ENTER':
        Tin[L[1]] = int(L[2])
    elif L[0]=='EXIT':
        Bill[L[1]] += int(L[2])-Tin[L[1]]
    else:  # CLOSE
        sys.stdout.write('Day %d\n' % day)
        for name,bill in sorted(Bill.items()):
            sys.stdout.write('%s $%.2f\n' % (name,bill/10))
        sys.stdout.write('\n')
