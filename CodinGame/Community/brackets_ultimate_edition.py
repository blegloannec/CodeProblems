#!/usr/bin/env python3

# not the shortest possible, but efficiently deals with inputs
# 100 times larger (in nb of brackets) than the given ones

U = {')':0,']':1,'}':2,'>':3,'(':0,'[':1,'{':2,'<':3}
B = {')':'(',']':'[','}':'{','>':'<','(':')','[':']','{':'}','<':'>'}
C = {')',']','}','>'}

def brackets(E):
    S = []
    F = []
    for c in E:
        if c in U:
            # validity check as in brackets_enhanced problem
            if S and S[-1]==U[c]:  # we pop asap
                S.pop()
            else:
                S.append(U[c])
            # simplify E removing already balanced parts
            if c in C and F and F[-1]==B[c]:
                F.pop()
            elif c in B:
                F.append(c)
    if S:  # balanceable iff S is empty at the end
        return -1
    # otherwise we have to balance the simplified expression F
    # (NB: when there is only one type of bracket, F is of the
    #  form ")..)(..(" )
    return dp(F,{},0,len(F)-1)

# O(n^2) DP embedding validity check to reduce branching
# (pretty efficient, deals with ')]>}'*500+'{<[('*500 in 1s)
def dp(F,memo,l,r):
    if r<l:
        return 0
    if (l,r) in memo:
        return memo[l,r]
    res = float('inf')
    if U[F[l]]==U[F[r]]:  # removing both ends
        res = min(res, dp(F,memo,l+1,r-1)+int(F[l] in C)+int(F[r] not in C))
    S = []  # validity check stack for F[l:m+1]
    for m in range(l,r):
        if S and U[F[m]]==S[-1]:
            S.pop()
        else:
            S.append(U[F[m]])
        if not S:  # F[l:m+1] is balanceable
            res = min(res, dp(F,memo,l,m)+dp(F,memo,m+1,r))
    memo[l,r] = res
    return res

def main():
    N = int(input())
    for _ in range(N):
        E = input()
        print(brackets(E))

main()
