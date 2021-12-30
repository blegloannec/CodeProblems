#!/usr/bin/env python3

def num(c):
    return ord(c)-ord('A')

D = []
memo = {}
def score(A):
    if A not in memo:
        memo[A] = sum(s for (w,s) in D if A&w==w)
    return memo[A]

def minimax(Q,A=0,B=0,alpha=float('-inf'),beta=float('inf'),maxi=True):
    if not Q:
        sa,sb = score(A),score(B)
        return ((sa-sb,sa,sb),-1)
    elif maxi:
        a = Q.pop()
        s = (minimax(Q,A|(1<<a),B,alpha,beta,False)[0],a)
        alpha = max(alpha,s[0][0])
        if Q and alpha<=beta:
            b = Q.pop()
            Q.append(a)
            s = max(s,(minimax(Q,A|(1<<b),B,alpha,beta,False)[0],b))
            Q.pop()
            Q.append(b)
        Q.append(a)
        return s
    else:
        a = Q.pop()
        s = (minimax(Q,A,B|(1<<a),True)[0],alpha,beta,a)
        beta = min(beta,s[0][0])
        if Q and alpha<=beta:
            b = Q.pop()
            Q.append(a)
            s = min(s,(minimax(Q,A,B|(1<<b),True)[0],alpha,beta,b))
            Q.pop()
            Q.append(b)
        Q.append(a)
        return s

def main():
    N,Q = map(int,input().split())
    S = [num(c) for c in reversed(input().split())]
    for _ in range(Q):
        w,s = input().split()
        scr = int(s)
        sig = 0
        for c in w:
            sig |= 1<<num(c)
        D.append((sig,scr))
    x,c = minimax(S)
    print('%s %d-%d' % (chr(c+ord('A')),x[1],x[2]))

main()
