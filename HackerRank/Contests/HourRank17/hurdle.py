#!/usr/bin/env python

import sys

n,k = map(int,sys.stdin.readline().split())
H = map(int,sys.stdin.readline().split())
print max(0,max(H)-k)
