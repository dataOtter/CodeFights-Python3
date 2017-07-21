"""Conway's Game of Life is a zero-player game that simulates a population of growing cells.
Every cell interacts with its neighbors, which are the cells that are
vertically, horizontally, or diagonally adjacent.
 At each step in time, the following changes take place:
    Any live cell with fewer than two live neighbors dies (to simulate underpopulation);
    Any live cell with two or three live neighbors lives on to the next generation;
    Any live cell with more than three live neighbors dies (to simulate overpopulation);
    Any dead cell with exactly three live neighbors becomes a live cell (to simulate reproduction).
In this challenge, the initial population is represented as a matrix of integers,
seed, where 0 indicates a dead cell and 1 indicates a live cell.
Your task here is to find the next population's pattern after one step in time."""
import numpy as np


def next_game_of_life(seed):
    """Input: seed only contains arrays of 1's and 0's.
    Guaranteed constraints: 1≤ seed.length ≤ 100, 1≤ seed[i].length ≤ 100,
    All seed[i].length are guaranteed to be the same, no matter what i is.
    Output: Returns an array that shows what seed looks like after one step."""
    num_columns = len(seed[0])
    next_stage = []

    for row_index in range(len(seed)):
        next_stage.append(get_new_row_state(seed, row_index, num_columns))

    return next_stage


def get_new_row_state(seed, row_index, num_columns):
    counters = []
    row = seed[row_index]
    counter_row = get_counter_row(row, num_columns)

    if row_index != 0:
        row_above = seed[row_index - 1]
        counter_above = get_counter_row(row_above, num_columns)
    else:
        counter_above = [0] * num_columns

    if row_index != len(seed)-1:
        row_below = seed[row_index + 1]
        counter_below = get_counter_row(row_below, num_columns)
    else:
        counter_below = [0] * num_columns

    for i in range(num_columns):
        counters.append(counter_row[i] - row[i] + counter_above[i] + counter_below[i])

    next_stage_row = get_new_states(counters, row)

    return next_stage_row


def get_new_states(counters, row):
    new_row = []

    for i in range(len(row)):
        c = counters[i]
        new_state = 0
        if row[i]:
            if c == 2 or c == 3:
                new_state = 1
        else:
            if c == 3:
                new_state = 1
        new_row.append(new_state)

    return new_row


def get_counter_row(row, num_columns):
    counters = []

    for ci in range(num_columns):
        c = 0
        if ci != 0 and row[ci - 1] == 1:
            c += 1
        if row[ci] == 1:
            c += 1
        if ci != num_columns - 1 and row[ci + 1] == 1:
            c += 1
        counters.append(c)

    return counters


s = [[0,0,0],
    [1,1,1],
    [0,0,0]]

print(np.array(s))

s = next_game_of_life(s)

print(np.array(s))

s = next_game_of_life(s)

print(np.array(s))
