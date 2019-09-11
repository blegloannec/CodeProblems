#!/usr/bin/env python3

# Very interesting and tricky problem!
# The simplest approach is to consider the construction of and optimal frequency array
# Freq (of size A and sum L) for the solution.
# 1. To maximize the score, this array can be considered non-decreasing.
# 2. The ">=D values among any N-subset" <=> sum_v Freq[v] < N for any (D-1)-subset of A
#    Keeping 1. in mind, to maximize the score, the sum of the freq of the last D-1 values
#    of A should be maximal, i.e. N-1, and (any other (D-1)-subset having a <= sum) this
#    immediately implies that the condition is verified on the whole Freq.
# 3. If p = A-(D-1)+1 and x = Freq[p], we shoud set
#    Freq[p:] = [x x ..(D-2 times).. x y] with y = N-1 - (D-2)*x (which must also be >=x)
#    and Freq[:p] of the form [0 0 .. 0 r x x .. x] (summing to L-(N-1)).
#    That Freq maximizes the score for a given x and the corresponding score can easily
#    be computed in O(1) (without explicitly building Freq).
# 3. To find the best x, try them all in O(L).

def collection(L,A,N,D):
    assert 1<=D<=N<=L
    if D==1:
        return L*A
    res = 0
    for x in range(L+1):
        if (D-1)*x<=N-1 and (A-(D-1))*x+(N-1)>=L:
            FA = N-1 - (D-2)*x
            q,r = divmod(L-FA, x)
            score = r*(A-q-1) + x*(A-q + A-1)*q//2 + FA*A
            res = max(res, score)
    return res

def main():
    T = int(input())
    for _ in range(T):
        L,A,N,D = map(int,input().split())
        res = collection(L,A,N,D)
        print(res or 'SAD')

main()
