"""You are given an array of integers.
On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a strictly increasing sequence from the input."""


def array_change(array_in):
    """Input: array.integer array_in.
    Guaranteed constraints: 3 ≤ array_in.length ≤ 105, -105 ≤ array_in[i] ≤ 105.
    Output: integer. The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.
    It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type."""
    counter = 0
    for i in range(len(array_in)-1):
        a = array_in[i]
        b = array_in[i + 1]
        if a >= b:
            c = a-b+1
            counter += c
            array_in[i + 1] += c

    return counter

arr = [2, 1, 10, 1]
print(array_change(arr))
