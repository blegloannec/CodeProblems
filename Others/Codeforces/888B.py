#!/usr/bin/env python3

from collections import Counter

n = int(input())
C = Counter(input())
print(n-abs(C['L']-C['R'])-abs(C['U']-C['D']))
