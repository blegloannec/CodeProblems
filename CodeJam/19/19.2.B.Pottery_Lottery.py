#!/usr/bin/env pypy

import sys, random
random.seed()
from heapq import *

def send(S):
    print S
    sys.stdout.flush()

def case():
    ExcludedVases = 15
    TokensPerVase = 4
    for V in xrange(1,ExcludedVases+1):
        for _ in xrange(TokensPerVase):
            day = int(raw_input())
            P = random.randint(1,100)
            send('%d %d' % (V,P))
    Content = []
    for V in xrange(1,21):
        day = int(raw_input())
        send('%d 0' % V)
        Content.append(map(int,raw_input().split()))
    mine = min((len(C),V+1) for V,C in enumerate(Content) if len(C)==len(set(C)))[1]
    H = [(len(C),V+1) for V,C in enumerate(Content) if V+1!=mine]
    heapify(H)
    while True:
        day = int(raw_input())
        if day==100:
            break
        S,V = heappop(H)
        P = random.randint(1,100)
        send('%d %d' % (V,P))
        heappush(H,(S+1,V))
    send('%d 100' % mine)

if __name__=='__main__':
    T = int(raw_input())
    for _ in xrange(T):
        case()
