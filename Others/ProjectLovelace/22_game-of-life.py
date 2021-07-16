def game_of_life(board, steps):
    H = len(board)
    W = len(board[0])
    for _ in range(steps):
        new_board = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                nv = -board[i][j]
                for vi in (i-1,i,i+1):
                    for vj in (j-1,j,j+1):
                        nv += board[vi%H][vj%W]
                if board[i][j]==1:
                    new_board[i][j] = int(2<=nv<=3)
                else:
                    new_board[i][j] = int(nv==3)
        board = new_board
    return board