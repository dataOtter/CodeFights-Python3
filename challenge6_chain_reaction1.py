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
    if r == 0:
        if b[r][c] == 2:
            if c == 0:
                b[r][c] = 0
                add_element(b, r + 1, c)
                add_element(b, r, c + 1)
            elif c == n - 1:
                b[r][c] = 0
                add_element(b, r + 1, c)
                add_element(b, r, c - 1)
        elif b[r][c] == 3:
            b[r][c] = 0
            add_element(b, r + 1, c)
            add_element(b, r, c - 1)
            add_element(b, r, c + 1)

    elif r == n - 1:
        if b[r][c] == 2:
            if c == 0:
                b[r][c] = 0
                add_element(b, r - 1, c)
                add_element(b, r, c + 1)
            elif c == n - 1:
                b[r][c] = 0
                add_element(b, r - 1, c)
                add_element(b, r, c - 1)
        elif b[r][c] == 3:
            b[r][c] = 0
            add_element(b, r - 1, c)
            add_element(b, r, c - 1)
            add_element(b, r, c + 1)

    elif b[r][c] == 4:
        b[r][c] = 0
        add_element(b, r - 1, c)
        b[r + 1][c] += 1
        add_element(b, r, c - 1)
        add_element(b, r, c + 1)


def add_element(b, r, c):
    b[r][c] += 1



moves = [[0, 0], [0, 0]]
print(chainReaction1(4, moves))
