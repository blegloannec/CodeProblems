#!/usr/bin/env python3

# long. incr. seq. with only 26 values

S = [ord(c)-ord('a') for c in input()]
Chain = [0]*26
for c in S:
    Chain[c] = max(Chain[:c], default=0) + 1
print(26 - max(Chain))
