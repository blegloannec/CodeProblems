#!/usr/bin/env pypy

import sys, random
random.seed()

S = 10**9

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

def send_pt_recv(p):
    return send_recv('%d %d\n' % p)

def rand_pt():
    return (random.randint(-S,S), random.randint(-S,S))

make_pt_x = lambda y: lambda x: (x,y)
make_pt_y = lambda x: lambda y: (x,y)

class CenterFound(Exception):
    pass

def dicho(l, r, left_side, make_pt):
    while r-l>1:
        m = (l+r)//2
        p = make_pt(m)
        ans = send_pt_recv(p)
        if ans=='CENTER':
            raise CenterFound
        elif ans==left_side:
            l = m
        else:
            r = m
    return l

def case():
    # randomly looking for a point inside the circle
    # (expectation <= 16/pi ~ 5 tries)
    while True:
        x0,y0 = p0 = rand_pt()
        ans = send_pt_recv(p0)
        if ans=='CENTER':
            return True
        elif ans=='HIT':
            break
    # binary searching for the horizontal and vertical borders
    # of the circle from that point
    try:
        xl = dicho(-S, x0, 'MISS', make_pt_x(y0))+1
        xr = dicho(x0,  S,  'HIT', make_pt_x(y0))
        yl = dicho(-S, y0, 'MISS', make_pt_y(x0))+1
        yr = dicho(y0,  S,  'HIT', make_pt_y(x0))
    except CenterFound:
        return True
    # the center is in the middle on both axis
    c = ((xl+xr)//2, (yl+yr)//2)
    return send_pt_recv(c)=='CENTER'

def main():
    T,A,B = map(int, recv().split())
    for t in xrange(1,T+1):
        assert case()

main()
