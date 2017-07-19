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

def nextGameOfLife(seed):
    """Input: seed only contains arrays of 1's and 0's.
    Guaranteed constraints: 1≤ seed.length ≤ 100, 1≤ seed[i].length ≤ 100,
    All seed[i].length are guaranteed to be the same, no matter what i is.
    Output: Returns an array that shows what seed looks like after one step."""
    num_rows = len(seed)
    num_columns = len(seed[0])
    next_stage = [[]]

    for row_index in range(num_rows):
        row = seed[row_index]
        row_above = seed[max(row_index-1, 0)]
        row_below = seed[min(row_index+1, num_rows)]

        if row_index == 0:
            get_neighbors_first_row(row, row_below, num_columns)
        elif row_index == num_rows:
            get_neighbors_last_row()
        else:
            next_stage.append(get_neighbors_row(row, row_above, row_below, num_columns)


def get_neighbors_first_row(row, row_below, num_columns, next_stage_row):
    counter = 0
    for ci in range(num_columns):
        if row[ci - 1]:
            counter += 1
        if row[ci + 1]:
            counter += 1

        if row_below[ci - 1]:
            counter += 1
        if row_below[ci]:
            counter += 1
        if row_below[ci + 1]:
            counter += 1

        next_stage_row.append(get_new_state(counter, row[ci]))


def get_neighbors_row(row, row_above, row_below, num_columns):

    counter_row = get_counter_row(row, num_columns)
    counter_above = get_counter_neighboring_row(row_above, num_columns)
    counter_below = get_counter_neighboring_row(row_below, num_columns)

    counters = np.array(counter_row) + np.array(counter_above) + np.array(counter_below)

    next_stage_row = get_new_states(counters, row)

    return next_stage_row


def get_new_states(counters, row):
    new_row = []

    for i in range(len(row)):
        c = counters[i]
        new_state = 0
        if row[i]:
            if c == 2 and c == 3:
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
        if row[ci - 1]:
            c += 1
        if row[ci + 1]:
            c += 1
        counters.append(c)

    return counters


def get_counter_neighboring_row(row, num_columns):
    counters = []

    for ci in range(num_columns):
        c = 0
        if row[ci - 1]:
            c += 1
        if row[ci]:
            c += 1
        if row[ci + 1]:
            c += 1
        counters.append(c)

    return counters


s = [[0,1,0],
 [0,1,0],
 [0,1,0]]
#nextGameOfLife(s)

a = np.array([1,2,3])
b = np.array([1,2,4])
print(a+b)
