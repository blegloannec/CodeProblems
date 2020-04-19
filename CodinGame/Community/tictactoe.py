#!/usr/bin/env python3

def fill(G):
    for i in range(3):
        for j in range(3):
            if G[i][j]=='.' and \
               (G[i][(j+1)%3]==G[i][(j+2)%3]=='O' or \
                G[(i+1)%3][j]==G[(i+2)%3][j]=='O' or \
                (i==j and G[(i+1)%3][(j+1)%3]==G[(i+2)%3][(j+2)%3]=='O') or \
                (i+j==2 and G[(i+1)%3][(j-1)%3]==G[(i+2)%3][(j-2)%3]=='O')):
                G[i][j] = 'O'
                return True
    return False

def main():
    G = [list(input()) for _ in range(3)]
    if fill(G):
        print('\n'.join(''.join(L) for L in G))
    else:
        print('false')

main()
