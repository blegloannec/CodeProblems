#!/usr/bin/env python3

inf = float('inf')
trace_count = 0

def minimax(depth=0, path=0, alpha=-inf, beta=inf, maxi=True):
    global trace_count
    trace_count += 1
    if depth==D:
        return Score[path]
    elif maxi:
        s = -inf
        b = 0
        while b<B and alpha<beta:
            s = max(s,minimax(depth+1,path*B+b,alpha,beta,False))
            alpha = max(alpha,s)
            b += 1
    else:
        s = inf
        b = 0
        while b<B and alpha<beta:
            s = min(s,minimax(depth+1,path*B+b,alpha,beta,True))
            beta = min(beta,s)
            b += 1
    return s

def main():
    global D,B,Score
    D,B = map(int,input().split())
    Score = list(map(int,input().split()))
    print(minimax(),trace_count)

main()
