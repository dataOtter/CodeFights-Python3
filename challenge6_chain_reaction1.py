"""You might have played Chain Reaction Game.
This series of challenges will consist of 2 parts.
In this part of challenge you have to return only final state of game, and this part is one player game.
There are 2 arguments - n is a number of rows and columns, moves is a list of positions where player place his orbs.
There are such rules:
    Once a cell has reached critical mass the orbs explode into the surrounding cells;
    Critical mass:
        2 for each corner,
        3 when touched any side,
        4 when anywhere except above positions."""


def chainReaction1(n, moves):
    """Input: integer n. The number of rows and columns. Guaranteed constraints: 4 ≤ n ≤ 300.
    array.array.integer moves. The list of positions. Guaranteed constraints:
    2 ≤ moves.length ≤ 5 · 104, moves[i].length = 2, 0 ≤ moves[i][j] < n.
    Output: array.array.integer. Final state of game"""
    board = []
    for i in range(n):
        board.append([0] * n)

    for move in moves:
        r, c = move[0], move[1]
        board[r][c] += 1
        if board[r][c] > 1:
            check(board, n, r, c)

    return board


def check(b, n, r, c):
    t = threshhold(r, c, n)
    if b[r][c] == t:
        b[r][c] = 0
        pos = positions(r, c, n)
        for p in pos:
            nr, nc = p[0], p[1]
            b[nr][nc] += 1
            check(b, n, nr, nc)
        #for p in pos:
            #check(b, n, p[0], p[1])


def threshhold(r, c, n):
    t = 4
    if r == 0:
        t -= 1
    elif r == n - 1:
        t -= 1
    if c == 0:
        t -= 1
    elif c == n - 1:
        t -= 1
    return t


def positions(r, c, n):
    p = []
    if r > 0:
        p.append([r - 1, c])
    if r < n - 1:
        p.append([r + 1, c])
    if c > 0:
        p.append([r, c - 1])
    if c < n - 1:
        p.append([r, c + 1])
    return p


moves = [[1,1],
 [1,2],
 [1,1],
 [1,2],
 [1,1],
 [1,2],
 [1,1]]
print(chainReaction1(4, moves))
