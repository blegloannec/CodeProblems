#!/usr/bin/env python3

def append_col(T, i, c):
    for L in T: L.append(' ')
    T[i][-1] = c

def main():
    N = int(input())+2
    M = [1]+list(map(int, input().split()))+[1]
    m0 = min(M)
    Out = [[] for _ in range(max(M)-m0+1)]
    for i in range(1, N):
        if M[i-1]<M[i]:
            for k in range(M[i-1], M[i]):
                append_col(Out, k-m0, '/')
        else:
            for k in range(M[i-1]-1, M[i]-1, -1):
                append_col(Out, k-m0, '\\')
        append_col(Out, M[i]-m0, '/')
        append_col(Out, M[i]-m0, '\\')
    for L in reversed(Out):
        print(''.join(L[:-2]).rstrip())

main()
