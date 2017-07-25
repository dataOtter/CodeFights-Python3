"""CFBot stores all of her important information in the Secret Archives.
CodeMaster is trying to pick the lock! The lock, a metal rectangle composed of movable cells,
is unique and hard to pick. Some of the lock’s cells are occupied, and some are empty.
The lock is unlocked when its occupied cells form a specific configuration.
The lock is represented as a matrix. The lock’s occupied cells are represented by
an uppercase English letter A-Z and its empty cells are represented by ..
When CodeMaster puts a magnet on one of the lock’s sides, all the occupied cells shift
toward that end of the lock. The sequence of actions is a string that can contain
the uppercase English letters L (left), R (right), D (down), and U (up),
which represent the side of the lock that CodeMaster places the magnet on.
Given the initial state of the lock and a sequence of actions,
your function should return the final state of the lock to the Secret Archives."""


def secret_archives_lock(lock, actions):
    """Input: array.string lock, string actions. The lock’s occupied cells are represented
    by an uppercase English letter A-Z and its empty cells are represented by ..
    Guaranteed constraints: 1 ≤ lock.length ≤ 300, 1 ≤ lock[i].length ≤ 300.
    Each element in this string is L, R, D, or U (left, right, down, or up),
    and indicates the side of the lock on which CodeMaster has placed the magnet.
    Guaranteed constraints: 1 ≤ actions.length ≤ 50.
    Output: array.string. The final state of the lock to the Secret Archives."""
    lck = []
    positions = []
    rows = len(lock)
    columns = len(lock[0])

    for i in range(rows):
        lck.append(list(lock[i]))    # turn the list of strings lock into a list of lists lck
        for j in range(columns):
            if lck[i][j] != '.':
                positions.append([i, j])    # put all letter positions in a list of lists, in order of appearance

    for char in actions:
        if char == 'L':
            move_left(lck, positions)
            print(lck)
        elif char == 'R':
            move_right(lck, positions, columns)
            print(lck)
        elif char == 'D':
            move_down(lck, positions, rows)
            print(lck)
        elif char == 'U':
            move_up(lck, positions)
            print(lck)

    for i in range(rows):
        lck[i] = ''.join(lck[i])

    return lck


def move_left(lk, pos):
    """Input: lock array l, list of letter position tuples pos
    Output: Moves all letters as far left as possible"""
    for i in range(len(pos)):
        x, y = pos[i][0], pos[i][1]    # set x and y to equal the coordinates/position of a letter in the array lock
        if y != 0:    # if the letter is not already located on the left edge of the array lock
            try:
                new_y = lk[x].index('.')    # find first empty position in row x
            except ValueError:
                break
            if new_y < y:    # if it is to left of current letter
                pos[i] = move_letter(lk, x, x, y, new_y)
    sort_positions(pos)


def move_right(lk, pos, c):
    """Input: lock array l, list of letter position tuples pos
    Output: Moves all letters as far right as possible"""
    i = len(pos) - 1
    while i >= 0:  # go through the list of positions backwards in order to get the rightmost letters first for each row
        x, y = pos[i][0], pos[i][1]    # set x and y to equal the coordinates/position of each letter in array lock
        if y != c - 1:    # if the letter is not already located on the right edge of the array lock
            try:
                new_y = lk[x][::-1].index('.')    # find last empty position in row x
            except ValueError:
                break
            if new_y > y:    # if it is to right of current letter
                pos[i] = move_letter(lk, x, x, y, new_y)
        i -= 1
    sort_positions(pos)


def move_down(lk, pos, r):
    """Input: lock array l, list of letter position tuples pos
    Output: Moves all letters as far down as possible"""
    i = len(pos) - 1
    no_dot = True
    while i >= 0:  # go through the list of positions backwards in order to get the bottom letters first for each column
        x, y = pos[i][0], pos[i][1]    # set x and y to equal the coordinates/position of a letter in the array lock
        dot = x
        if x != r - 1:    # if the letter is not already located on the bottom edge of the array lock
            if no_dot:
                new_x = r - 1
                while new_x > x:    # look only below current letter
                    if lk[new_x][y] == '.':    # find first empty position in column y, if any
                        pos[i] = move_letter(lk, x, new_x, y, y)
                        dot = new_x
                        no_dot = False
                        break
                    new_x -= 1
                no_dot = False
            else:
                dot -= 1
                pos[i] = move_letter(lk, x, dot, y, y)
        i -= 1
    sort_positions(pos)


def move_up(lk, pos):
    """Input: lock array l, list of letter position tuples pos
    Output: Moves all letters as far up as possible"""
    for i in range(len(pos)):
        x, y = pos[i][0], pos[i][1]    # set x and y to equal the coordinates/position of a letter in the array lock
        if x != 0:    # if the letter is not already located on the top edge of the array lock
            for new_x in range(x):    # look only above current letter
                if lk[new_x][y] == '.':    # find first empty position in column y, if any
                    pos[i] = move_letter(lk, x, new_x, y, y)
                    break
    sort_positions(pos)


def move_letter(lck, x, new_x, y, new_y):
    letter = lck[x][y]
    lck[new_x][new_y] = letter  # move the letter to that empty position
    lck[x][y] = "."
    return [new_x, new_y]  # update the list of positions


def sort_positions(p):
    p.sort(key=lambda x: (x[0], x[1]))

l = ["...PD.O..P",
 ".MF.......",
 "Q.....I...",
 "....JNJ...",
 ".Y..O.O.J.",
 "V..U......",
 "..J..H....",
 "....T.J...",
 "W.....A.B.",
 ".P....O.K."]

l2 = ["..A.",
      ".BC.",
      "....",
      "...D"]

l3 = ["AB", "CD"]

actions = "RURLD"

print(secret_archives_lock(l2, actions))
