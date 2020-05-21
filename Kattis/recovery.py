#!/usr/bin/env python3

def main():
    Row = list(map(int, input()))
    Col = list(map(int, input()))
    H, W = len(Row), len(Col)
    M = [[1]*W for _ in range(H)]
    InvalidRows = [i for i in range(H) if Row[i]!=W&1]
    InvalidCols = [j for j in range(W) if Col[j]!=H&1]
    IRS, ICS = len(InvalidRows), len(InvalidCols)
    if (IRS+ICS)&1:
        print(-1)
        return
    # pairing the columns in excess at a cost of 2 ones over row 0
    if IRS<ICS:
        InvalidRows = [0]*(ICS-IRS) + InvalidRows
    # or pairing the rows in excess at a cost of 2 ones over column 0
    if IRS>ICS:
        InvalidCols = [0]*(IRS-ICS) + InvalidCols
    # greedily pairing invalid rows & columns to fix them at a cost of 1 one
    for i,j in zip(InvalidRows, InvalidCols):
        M[i][j] = 0
    print('\n'.join(''.join(map(str, L)) for L in M))

main()
