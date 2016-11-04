#!/usr/bin/env python

import sys

H = map(int,sys.stdin.readline().split())
W = map((lambda c: H[ord(c)-ord('a')]), list(sys.stdin.readline().strip()))
print max(W)*len(W)
