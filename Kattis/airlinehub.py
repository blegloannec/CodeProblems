#!/usr/bin/env python3

from math import *
import sys
input = sys.stdin.readline

# https://en.wikipedia.org/wiki/Haversine_formula
def haversine(A,B):  # for normalized radius 1
    lat1,lon1,coslat1 = A
    lat2,lon2,coslat2 = B
    sindlat = sin((lat1-lat2)/2.)
    sindlon = sin((lon1-lon2)/2.)
    return 2.*asin(sqrt(sindlat*sindlat + coslat1*coslat2*sindlon*sindlon))

def main():
    while True:
        try:
            N = int(input())
        except ValueError:
            break
        P = [tuple(map(float, input().split())) for _ in range(N)]
        Prad = []
        for p in P:
            lat,lon = map(radians, p)
            coslat = cos(lat)
            Prad.append((lat,lon,coslat))
        D = [[0.]*N for _ in range(N)]
        for i in range(N):
            for j in range(i+1,N):
                D[i][j] = D[j][i] = haversine(Prad[i], Prad[j])
        minmaxd = float('inf')
        for i in range(N):
            maxdi = max(D[i])
            if maxdi<=minmaxd:
                minmaxd = maxdi
                besti = i
        sys.stdout.write('%.2f %.2f\n' % P[besti])

main()
