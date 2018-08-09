#!/usr/bin/env python3

import sys
from itertools import cycle

try:
    K = bytes.fromhex(open(sys.argv[1],'r').read().strip())
    M = sys.stdin.buffer.read()
    sys.stdout.buffer.write(bytes(c^k for c,k in zip(M,cycle(K))))
except:
    sys.stderr.write('usage: python3 %s key_file < data_in > data_out\n' % sys.argv[0])
    sys.exit(1)
