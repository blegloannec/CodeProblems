#!/usr/bin/env python3

def sqrt_walk(N):
    assert N>0
    N -= 1
    W = [(1,1)]
    k = 1
    while N>=k:  # second column
        W.append((k+1,2))
        N -= k
        k += 1
    while N>0:  # first column
        W.append((k,1))
        N -= 1
        k += 1
    return W

def log_walk(N):
    assert N>30
    M = (N-30)>>1
    W, w = [(1,1)], 1
    i = 2
    left = True
    while M:
        if M&1:
            W += [(i,k) for k in (range(1,i+1) if left else range(i,0,-1))]
            w += 1<<(i-1)
            left = not left
        else:
            W.append((i, (1 if left else i)))
            w += 1
        M >>= 1
        i += 1
    while w<N:
        W.append((i, (1 if left else i)))
        w += 1
        i += 1
    return W

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        W = sqrt_walk(N) if N<=30 else log_walk(N)
        #assert len(W)<=500
        print('Case #{}:'.format(t))
        for p in W:
            print(*p)
            a,b = p

main()
