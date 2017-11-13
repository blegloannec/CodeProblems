#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N,P = map(int,input().split())
        if P<=2:
            print('impossible')
        else:
            print(('a'+(P-2)*'b'+'a')*(N//P))

main()
