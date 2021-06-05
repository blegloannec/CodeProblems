#!/usr/bin/env python3

def near_pal_repl(W,i,j,joker=False):
    if i>=j:
        return joker
    if W[i]!=W[j]:
        return False if joker else near_pal_repl(W,i+1,j-1,True)
    return near_pal_repl(W,i+1,j-1,joker)

# NB: addition and removal are equivalent
def near_pal_rem(W,i,j,joker=False):
    if i>=j:
        return joker
    if W[i]!=W[j]:
        return False if joker else near_pal_rem(W,i+1,j,True) or near_pal_rem(W,i,j-1,True)
    return near_pal_rem(W,i+1,j-1,joker)

# NB: a palindrome is a near-palindrome by addition of the central letter if the size is odd
#     or removal of one of the 2 central letters if the size is even
def near_pal(W):
    return W==W[::-1] or near_pal_repl(W,0,len(W)-1) or near_pal_rem(W,0,len(W)-1)

def main():
    N = int(input())
    res = []
    for _ in range(N):
        W = input()
        res.append(str(int(near_pal(W))))
    print(''.join(res))

main()
