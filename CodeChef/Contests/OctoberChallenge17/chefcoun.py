#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        N = (1<<32)-3
        A = [N//(n-2)]*n
        A[1] = N%(n-2)
        A[0] = 1
        print(' '.join(map(str,A)))
        
main()
