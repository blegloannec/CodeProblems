#!/usr/bin/env python3

G = input().split(',')
C = input().split(',')
N = int(input())
D = {}
for _ in range(N):
    name, bars,beam,floor = input().split(',')
    if name not in D:
        D[name] = {'bars': bars, 'beam': beam, 'floor': floor}
    else:
        D[name]['bars']  = max(bars, D[name]['bars'])
        D[name]['beam']  = max(beam, D[name]['beam'])
        D[name]['floor'] = max(floor, D[name]['floor'])
for name in G:
    print(','.join(D[name][cat] for cat in C))
