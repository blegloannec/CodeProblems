#!/usr/bin/env python

import sys

# any way of cutting is minimal and uses n*m-1 cuts
n,m = map(int,sys.stdin.readline().split())
print n*m-1
