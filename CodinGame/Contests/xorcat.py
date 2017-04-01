#!/usr/bin/env python3

import sys

key = open(sys.argv[1],'r').read().strip()
K = [int(key[i*2:(i+1)*2],16) for i in range(len(key)//2)]
i = 0
for c in sys.stdin.read():
    sys.stdout.write(chr(ord(c)^K[i]))
    i = (i+1)%len(K)
