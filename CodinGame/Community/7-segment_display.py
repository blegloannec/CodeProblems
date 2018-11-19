#!/usr/bin/env python3

#  0
# 1 2
#  3
# 4 5
#  6

D7 = [0b1110111,0b0100100,0b1011101,0b1101101,0b0101110,0b1101011,0b1111011,0b0100101,0b1111111,0b1101111]
C = [' ',None]

def seg(c,i):
    return C[(D7[c]>>i)&1]

def dig(c):
    return [' '+seg(c,0)*S+' ']+[seg(c,1)+' '*S+seg(c,2)]*S+[' '+seg(c,3)*S+' ']+[seg(c,4)+' '*S+seg(c,5)]*S+[' '+seg(c,6)*S+' ']

def digs(N):
    return '\n'.join(' '.join(L).rstrip() for L in zip(*(dig(int(c)) for c in N)))

def main():
    global S
    N = input()
    C[1] = input()
    S = int(input())
    print(digs(N))

main()
