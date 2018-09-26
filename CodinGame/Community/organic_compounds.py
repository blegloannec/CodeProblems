#!/usr/bin/env python3

def valid(M):
    for i in range(0,len(M),2):
        for j in range(1,len(M[i]),6):
            if M[i][j]=='H':
                h = int(M[i][j+1])
                b = 0
                for bi,bj in [(i,j-3),(i,j+3),(i-1,j),(i+1,j)]:
                    if 0<=bi<len(M) and 0<=bj<len(M[bi]) and M[bi][bj]!=' ':
                        b += int(M[bi][bj])
                if b+h!=4:
                    return False
    return True

N = int(input())
M = [input() for _ in range(N)]
print('VALID' if valid(M) else 'INVALID')
