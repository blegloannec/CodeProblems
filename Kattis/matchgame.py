#!/usr/bin/env python3

D7 = [0b1110111,0b0100100,0b1011101,0b1101101,0b0101110,0b1101011,0b1111011,0b0100101,0b1111111,0b1101111]

ones = lambda x: bin(x).count('1')

def main():
    X,Y = input().split()
    assert len(X)==len(Y)
    D = [(D7[ord(x)-ord('0')],D7[ord(y)-ord('0')]) for x,y in zip(X,Y) if x!=y]
    ok = False
    if len(D)==1:
        x1,y1 = D[0]
        ok = (ones(x1)==ones(y1) and ones(x1^y1)==2)
    elif len(D)==2:
        (x1,y1),(x2,y2) = D
        ok = (ones(x1)+ones(x2)==ones(y1)+ones(y2) and ones(x1^y1)==1 and ones(x2^y2)==1)
    print('yes' if ok else 'no')

main()
