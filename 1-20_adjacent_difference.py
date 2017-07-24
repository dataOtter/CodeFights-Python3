"""Given an array of integers, find the maximal absolute difference between any two of its adjacent elements."""


def array_max_adjacent_difference(array_in):
    """Input: array.integer inputArray. Guaranteed constraints: 3 ≤ inputArray.length ≤ 10, -15 ≤ inputArray[i] ≤ 15.
    Output: Returns integer. The maximal absolute difference."""
    diff = 0
    for i in range(len(array_in)-1):
        temp_diff = abs(array_in[i] - array_in[i + 1])
        if temp_diff > diff:
            diff = temp_diff
    return diff

inputArray = [2, 4, 1, 0]
print(array_max_adjacent_difference(inputArray))
