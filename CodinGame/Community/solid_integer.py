#!/usr/bin/env python3

# Same as base 9 spreadsheet labelling (over 1-9 alphabet)
# see also "Spreadsheet Labels" & "Decode the message" on CG

# https://paradise.caltech.edu/ist4/lectures/foster%201947%20decimal%20no%20zero%20number%20system.pdf
# https://oeis.org/A052382

n = int(input())
O = []
while n:
    n,c = divmod(n-1, 9)
    O.append(c+1)
print(*reversed(O), sep='')
