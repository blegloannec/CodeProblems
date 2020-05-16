#!/usr/bin/env pypy

import sys

def reverse_dist(C, Time, Pred):
    Pred.sort()
    Time.sort()
    Dist = [None]*C
    Dist[0] = 0
    currv = currt = 1
    ip = it = 0
    while ip<len(Pred) or it<len(Time):
        if ip<len(Pred) and Pred[ip][0]==currv:
            currv0 = currv
            while ip<len(Pred) and Pred[ip][0]==currv0:
                Dist[Pred[ip][1]] = currt
                ip += 1
                currv += 1
        else:
            currt = Time[it][0]
            while it<len(Time) and Time[it][0]==currt:
                Dist[Time[it][1]] = currt
                it += 1
                currv += 1
        currt += 1
    return Dist

def main():
    T = int(sys.stdin.readline())
    for t in xrange(1,T+1):
        C,D = map(int, sys.stdin.readline().split())
        Pred = []
        Time = []
        for i,x in enumerate(map(int, sys.stdin.readline().split())):
            if x<0:
                Pred.append((-x, i+1))
            else:
                Time.append(( x, i+1))
        Dist = reverse_dist(C, Time, Pred)
        E = []
        for _ in range(D):
            u,v = map(int, sys.stdin.readline().split())
            e = abs(Dist[u-1] - Dist[v-1])
            E.append(10**6 if e==0 else e)
        sys.stdout.write('Case #%d: %s\n' % (t, ' '.join(map(str,E))))

main()
