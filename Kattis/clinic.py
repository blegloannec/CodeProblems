#!/usr/bin/env python3

from heapq import *
import sys
input = sys.stdin.readline

def main():
    N,K = map(int, input().split())
    Wait = []
    StillWait = set()
    for _ in range(N):
        Q,*L = input().split()
        if Q=='1':
            T,name,S = L
            prio = int(S) - K*int(T)
            heappush(Wait, (-prio, name))
            StillWait.add(name)
        elif Q=='2':
            while Wait and Wait[0][1] not in StillWait:
                heappop(Wait)
            if Wait:
                _,name = heappop(Wait)
                StillWait.remove(name)
                sys.stdout.write(f'{name}\n')
            else:
                sys.stdout.write('doctor takes a break\n')
        else:
            _,name = L
            StillWait.discard(name)

main()
