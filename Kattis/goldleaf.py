#!/usr/bin/env python3

# testing all horizontal folds in O(H^2) using masks
def fast_fold(H, W, B):  
    full = (1<<W)-1
    for f in range(H-1):
        valid = True
        for i in range(H):
            b = B[i]
            j = 2*f+1-i
            if 0<=j<H:
                b ^= B[j]
            valid = b==full
            if not valid:
                break
        if valid:
            return f
    return None

# testing one arbitrary fold in O(HW)
def fold(H, W, B, sym):
    for i in range(H):
        for j in range(W):
            si,sj = sym(i,j)
            if 0<=si<H and 0<=sj<W and (si,sj)!=(i,j):
                if B[i][j]==B[si][sj]:
                    return False
            elif not B[i][j]:
                return False
    return True

def diag_sym(k):
    # line y-x = k
    def sym(x,y):
        d = k - (y-x)
        return (x-d, y+d)
    return sym

def antidiag_sym(k):
    # line x+y = k
    def sym(x,y):
        d = k - (x+y)
        return (x+d, y+d)
    return sym

def case(H, W, G):
    Sol = []
    # horizontal
    B = [int(''.join(L), 2) for L in G]
    i = fast_fold(H, W, B)
    if i is not None:
        Sol.append((i+1,1, i+1,W))
    # vertical (transpose)
    B = [int(''.join(G[i][j] for i in range(H)), 2) for j in range(W)]
    j = fast_fold(W, H, B)
    if j is not None:
        Sol.append((1,j+1, H,j+1))
    # diagonal
    B = [[c=='1' for c in L] for L in G]
    for k in range(-(H-1), W):
        if fold(H, W, B, diag_sym(k)):
            x0,y0 = (1,k+1) if k>=0 else (-k+1,1)
            d = min(H-x0, W-y0)
            Sol.append((x0,y0, x0+d,y0+d))
    # anti-diag.
    for k in range(H+W-1):
        if fold(H, W, B, antidiag_sym(k)):
            x0,y0 = (k+1,1) if k<H else (H,k-(H-1)+1)
            d = min(x0-1, W-y0)
            Sol.append((x0,y0, x0-d,y0+d))
    return min(Sol)

def main():
    H,W = map(int, input().split())
    G = [['1' if c=='#' else '0' for c in input()] for _ in range(H)]
    print(*case(H, W, G))

main()
