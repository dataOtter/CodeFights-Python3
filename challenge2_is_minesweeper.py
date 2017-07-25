"""Each cell of Minesweeper gameboard can be:
    a mine (appears as 9)
    or a number representing the number of mines in its surrounding cells(a cell is considered
        as surrounding another cell when this cell meets that cell on at least 1 corner) (appears as 0 - 8)
Your task is to check whether a "gameboard" is a valid gameboard."""


def minesweeper1(gameboard):
    """Input: array.array.integer gameboard. Guaranteed constraints: 3 ≤ gameboard.length ≤ 100,
    3 ≤ gameboard[i].length ≤ 100, gameboard[i].length = gameboard[j].length, 0 ≤ gameboard[i][j] ≤ 9.
    Output: boolean true if the input array is a valid minesweeper gameboard."""
    rows = len(gameboard)
    columns = len(gameboard[0])

    mines = get_mine_locations(rows, gameboard)

    board2 = make_empty_board(rows, columns)

    for a, b in mines:
        board2[a][b] = 9    # add mine
        add_clues(a, b, board2, columns, rows)

    if gameboard == board2:
        valid = True
    else:
        valid = False

    return valid


def get_mine_locations(r, board):
    """Input: num rows r, original gameboard
    Output: Returns list of mine locations"""
    mines = []
    for i in range(r):
        for j, k in enumerate(board[i]):
            if k == 9:
                mines.append((i, j))
    return mines


def make_empty_board(r, c):
    """Input: num rows r, num columns c
    Output: Returns multi-dimensional array; a new, empty gameboard of the specified size"""
    board = []  # [[0] * columns] * rows -- indexing this does not work
    for x in range(r):
        board.append([])
        for y in range(c):
            board[x].append(0)
    return board


def add_clues(i, j, b, c, r):
    """Input: Mine row index i, mine column index j, gameboard b, num of columns c, num of rows r
    Output: Updates the gameboard with clues for the input mine"""
    add_clues_row(i, j, c, b)
    if i != 0:
        add_clues_row(i - 1, j, c, b)
    if i < r-1:
        add_clues_row(i + 1, j, c, b)


def add_clues_column(i, j, board):
    """Input: Row index i, column index j, gameboard
    Output: Updates the clue at the input location"""
    if board[i][j] != 9:
        board[i][j] += 1


def add_clues_row(i, j, c, board):
    """Input: Row index i, column index j, num columns c, gameboard
    Output: Updates the clues in the input row"""
    add_clues_column(i, j, board)
    if j != 0:
        add_clues_column(i, j - 1, board)
    if j < c - 1:
        add_clues_column(i, j + 1, board)

gameboard = [[0,0,0,0,0],
 [0,1,1,1,0],
 [0,1,9,1,0],
 [0,1,1,1,0],
 [0,0,0,0,0]]

print(minesweeper1(gameboard))
