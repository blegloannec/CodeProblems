#!/usr/bin/env python3

N = int(input())
P = list(map(float,input().split()))
E = [N*p for p in P]  # yep, trivial...
print(' '.join(map(str,E)))
