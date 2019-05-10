#!/usr/bin/env python3

# lame & unoriginal...
# lazy solution code mostly copy-pasted from the similar CG puzzle tetris.py

BH = int(input())
BW = int(input())
B = [input() for _ in range(BH)]
Bsize = sum(sum(int(c=='.') for c in L) for L in B)
PH = int(input())
PW = int(input())
P = [[y for y,c in enumerate(input()) if c=='#'] for _ in range(PH)]
Psize = sum(len(L) for L in P)
if Psize!=Bsize:
    print('HOLE')
else:
    full = False
    rotcnt = 0
    while not full and rotcnt<4:
        full = any(all(0<=i+x<BH and 0<=j+y<BW and B[i+x][j+y]=='.' for x in range(PH) for y in P[x]) \
                   for i in range(-PH+1,BH+PH) for j in range(-PW+1,BW+PW))
        # rotation
        B = [''.join(B[i][j] for i in range(BH)) for j in range(BW-1,-1,-1)]
        BH,BW = BW,BH
        rotcnt += 1
    print('FULL' if full else 'HOLE')
