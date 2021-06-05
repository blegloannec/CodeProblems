#!/usr/bin/env python3

import re

W,H = map(int, input().split())
G = [re.sub(r'[^.X]', '*', input()) for _ in range(H)]

if G[0][0]==G[0][-1]==G[-1][0]==G[-1][-1]:
    print('Rectangle' if G[0][0]=='X' else 'Ellipse')
else:
    print('Triangle')
