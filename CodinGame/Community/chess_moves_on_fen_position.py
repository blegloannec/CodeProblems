#!/usr/bin/env python3

class Chessboard:
    def __init__(self, FEN):
        self.Board = [['.']*8 for _ in range(8)]
        FEN = FEN.split('/')
        for i in range(8):
            j = 0
            for c in FEN[i]:
                if '1'<=c<='8':
                    j += ord(c)-ord('0')
                else:
                    self.Board[i][j] = c
                    j += 1
    
    def FEN(self):
        O = []
        for i in range(8):
            L = []
            j = 0
            while j<8:
                if self.Board[i][j]=='.':
                    j0 = j
                    while j<8 and self.Board[i][j]=='.':
                        j += 1
                    L.append(str(j-j0))
                else:
                    L.append(self.Board[i][j])
                    j += 1
            O.append(''.join(L))
        return '/'.join(O)
    
    def coords(self, li):
        return  7-(ord(li[1])-ord('1')), ord(li[0])-ord('a')
    
    def move(self, MOVE):
        i0,j0 = self.coords(MOVE[:2])
        i1,j1 = self.coords(MOVE[2:4])
        if self.Board[i0][j0] in 'Kk' and abs(j0-j1)>1:  # castling
            if j1>j0:
                self.Board[i0][j1-1] = self.Board[i0][7]
                self.Board[i0][7] = '.'
            else:
                self.Board[i0][j1+1] = self.Board[i0][0]
                self.Board[i0][0] = '.'
        if self.Board[i0][j0] in 'Pp' and self.Board[i1][j1]=='.' and j0!=j1:  # en passant
            self.Board[i0][j1] = '.'
        if len(MOVE)==5:  # promotion
            self.Board[i1][j1] = MOVE[4]
        else:
            self.Board[i1][j1] = self.Board[i0][j0]
        self.Board[i0][j0] = '.'


if __name__=='__main__':
    CB = Chessboard(input())
    N = int(input())
    for _ in range(N):
        CB.move(input())
    print(CB.FEN())
