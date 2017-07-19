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


def nextGameOfLife(seed):
    """Input: seed only contains arrays of 1's and 0's.
    Guaranteed constraints: 1≤ seed.length ≤ 100, 1≤ seed[i].length ≤ 100,
    All seed[i].length are guaranteed to be the same, no matter what i is.
    Output: Returns an array that shows what seed looks like after one step."""
    