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
import numpy as np
import array


def make_transfers_board():
    n2 = 3 * 50000
    board = [0] * n2
    board_array = array.array('i', board)
    return board_array


transfers = make_transfers_board()


def add_transfer(tc, tr, am):
    global transfers_count
    global fastindex
    # print("schedule transfer {} to col {} row {} amount {}".format(transfers_count, tc, tr, am))
    # print(str(transfers_count))
    key = str(tc) + "," + str(tr)
    if key in fastindex:
        lookup = fastindex[key]
        transfers[3 * lookup + 2] += am
    else:
        transfers[3 * transfers_count + 0] = tc
        transfers[3 * transfers_count + 1] = tr
        transfers[3 * transfers_count + 2] = am
        fastindex[key] = transfers_count
        transfers_count += 1


def clear_all_transfers():
    global transfers_count
    global fastindex
    # print("clearing transfers_count from {}".format(transfers_count))
    transfers_count = 0
    # print("to {}".format(transfers_count))
    fastindex = {"-1,-1": -1}


new_transfers = make_transfers_board()
new_fastindex = {"-1,-1": -1}


def add_new_transfer(tc, tr, am):
    global new_transfers_count
    global new_fastindex
    key = str(tc) + "," + str(tr)
    if key in new_fastindex:
        lookup = new_fastindex[key]
        new_transfers[3 * lookup + 2] += am
    else:
        new_transfers[3 * new_transfers_count + 0] = tc
        new_transfers[3 * new_transfers_count + 1] = tr
        new_transfers[3 * new_transfers_count + 2] = am
        new_fastindex[key] = new_transfers_count
        new_transfers_count += 1
        # print("schedule transfer {} to col {} row {} amount {}".format(transfers_count, tc, tr, am))
        # print(str(transfers_count))


def clear_all_new_transfers():
    global new_transfers_count
    global new_fastindex
    # print("clearing transfers_count from {}".format(transfers_count))
    new_transfers_count = 0
    # print("to {}".format(transfers_count))
    new_fastindex = {"-1,-1": -1}


def copy_new_transfers_into_transfers():
    global transfers_count
    global new_transfers_count
    for one_transfer in range(new_transfers_count):
        transfers[3 * one_transfer + 0] = new_transfers[3 * one_transfer + 0]
        transfers[3 * one_transfer + 1] = new_transfers[3 * one_transfer + 1]
        transfers[3 * one_transfer + 2] = new_transfers[3 * one_transfer + 2]
    transfers_count = new_transfers_count


def do_all_transfers(b, n):
    global transfers_count
    for one_transfer in range(transfers_count):
        tc = transfers[3 * one_transfer + 0]
        tr = transfers[3 * one_transfer + 1]
        am = transfers[3 * one_transfer + 2]
        # print("doing transfer {} to col {} row {} amount {}".format(one_transfer, tc, tr, am))
        add_to_cell(b, n, tc, tr, am)


def convert_transfers_array_to_list():
    global transfers_count
    lst = []
    for one_transfer in range(transfers_count):
        tc = transfers[3 * one_transfer + 0]
        tr = transfers[3 * one_transfer + 1]
        am = transfers[3 * one_transfer + 2]
        lst.append([tc, tr, am])
    return lst


def add_transfers_list_to_array(lst):
    for triple in lst:
        add_transfer(triple[0], triple[1], triple[2])


def board_to_final_form(b, n):
    ans = []
    for c in range(n):
        row = []
        for r in range(n):
            row.append(get_cell(b, n, c, r))
        ans.append(row)
    return ans


def check_for_carryovers(b, n, c, r, tb, amount):
    # print("Checking row {} col {}".format(r,c))
    tb_rc = tb[n * r + c]
    b_rc = b[n * r + c]

    if b_rc >= tb_rc:
        transfer = b_rc // tb_rc
        b[n * r + c] = b_rc % tb_rc

        if c < n - 1: add_new_transfer(c + 1, r, transfer)
        if c > 0: add_new_transfer(c - 1, r, transfer)
        if r < n - 1: add_new_transfer(c, r + 1, transfer)
        if r > 0: add_new_transfer(c, r - 1, transfer)

    else:
        b[n * r + c] = b_rc


def check_list_pos(b, n, tb):
    done = False
    while not done:

        clear_all_new_transfers()
        for one_transfer in range(transfers_count):
            tc = transfers[3 * one_transfer + 0]
            tr = transfers[3 * one_transfer + 1]
            am = transfers[3 * one_transfer + 2]
            check_for_carryovers(b, n, tc, tr, tb, am)

        copy_new_transfers_into_transfers()
        do_all_transfers(b, n)

        if transfers_count == 0:
            done = True


def make_board(n):
    n2 = n * n
    board = [0] * n2
    board_array = array.array('i', board)
    return board_array


def make_t_board(n):
    n2 = n * n
    tb = [4] * n2
    tb_array = array.array('i', tb)

    for i in range(n):
        set_cell(tb_array, n, 0, i, 3)
        set_cell(tb_array, n, i, 0, 3)
        set_cell(tb_array, n, n - 1, i, 3)
        set_cell(tb_array, n, i, n - 1, 3)

    set_cell(tb_array, n, 0, 0, 2)
    set_cell(tb_array, n, n - 1, 0, 2)
    set_cell(tb_array, n, 0, n - 1, 2)
    set_cell(tb_array, n, n - 1, n - 1, 2)
    return tb_array


def get_cell(b, n, c, r):
    return b[n * r + c]


def add_to_cell(b, n, c, r, val):
    b[n * r + c] += val


def set_cell(b, n, c, r, val):
    b[n * r + c] = val


def chainReaction1(n, moves):
    global transfers_count
    global new_transfers_count
    global fastindex
    global new_fastindex

    transfers_count = 0
    new_transfers_count = 0
    fastindex = {"-1,-1": -1}
    new_fastindex = {"-1,-1": -1}

    board = make_board(n)
    t_board = make_t_board(n)

    initial_triples = []
    for move in moves:
        initial_triples.append([move[0], move[1], 1])

    add_transfers_list_to_array(initial_triples)
    do_all_transfers(board, n)

    check_list_pos(board, n, t_board)

    return board_to_final_form(board, n)


def board_print(b):
    print(np.array(b))


moves = [[0,0],[1,0],[1,0],[0,1],[0,1],[1,1],[1,1],[1,1],[0,0]]
#moves = [[0,0],[0,0]]
after = chainReaction1(6, moves)
board_print(after)

