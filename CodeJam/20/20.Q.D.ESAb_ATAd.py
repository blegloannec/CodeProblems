#!/usr/bin/env python3

import sys

def recv():
    return sys.stdin.readline().strip()

def send(s):
    sys.stdout.write(s)
    #sys.stderr.write(s)
    if len(s)==0 or s[-1]!='\n':
        sys.stdout.write('\n')
        #sys.stderr.write('\n')
    sys.stdout.flush()

def send_recv(s):
    send(s)
    return recv()
    
def main():
    T,B = map(int,recv().split())
    for t in range(1,T+1):
        Data = [None]*B
        idx = qry = 0
        flip_idx = mirr_idx = -1  # reference indices for flip/mirror
        flip, mirr = 0, False
        while 2*idx<B:
            if qry>0 and qry%10==0:  # first 2 requests of the block of 10
                flip, mirr = 0, False
                if flip_idx>=0:  # checking flip
                    flip_ans = int(send_recv(str(flip_idx+1)))
                    flip = int(flip_ans != Data[flip_idx])
                else:
                    send_recv('1')
                if mirr_idx>=0:  # checking mirror
                    mirr_ans = int(send_recv(str(mirr_idx+1))) ^ flip
                    mirr = (mirr_ans != Data[mirr_idx])
                else:
                    send_recv('1')
            else:  # remaining 4 pairs of requests of the block of 10
                # left request
                Data[idx] = int(send_recv(str(idx+1 if not mirr else B-idx))) ^ flip
                # right request
                jdx = B-1-idx
                Data[jdx] = int(send_recv(str(jdx+1 if not mirr else B-jdx))) ^ flip
                # setting flip/mirror indices if not yet found
                if flip_idx<0 and Data[idx]==Data[jdx]:
                    flip_idx = idx
                elif mirr_idx<0 and Data[idx]!=Data[jdx]:
                    mirr_idx = idx
                idx += 1
            qry += 2
        res = ''.join(str(d^flip) for d in (Data if not mirr else reversed(Data)))
        assert send_recv(res) == 'Y'

main()
