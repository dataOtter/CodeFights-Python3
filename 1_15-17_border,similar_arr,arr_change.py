"""1-15 add border:
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

1-16 similar arrays:
Two arrays are called similar if one can be obtained from another
by swapping at most one pair of elements in one of the arrays.
Given two arrays a and b, check whether they are similar.

1-17 array change:
You are given an array of integers.
On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a strictly increasing sequence from the input."""


def add_border(picture):
    """Input: array.string picture. A non-empty array of non-empty equal-length strings.
    Guaranteed constraints: 1 ≤ picture.length ≤ 5, 1 ≤ picture[i].length ≤ 5.
    Output: Returns array.string, the same matrix of characters, framed with a border of asterisks of width 1."""
    width = len(picture[0]) + 2
    border = ['*' * width]

    for s in picture:
        border.append("*" + s + "*")
    border.append(border[0])

    return border

picture = ["abc", "ded"]
print(add_border(picture))


def are_similar(a: list, b: list):
    """Input: array.integer a, b. Guaranteed constraints: 3 ≤ a.length ≤ 105, 1 ≤ a[i] ≤ 1000,
    b.length = a.length, 1 ≤ b[i] ≤ 1000.
    Output: Returns boolean true if a and b are similar, false otherwise."""
    similar = False
    if a == b:
        similar = True
    # If the arrays are the same when sorted, there is no need to compare out-of-place elements,
    # only check that there is no more than one pair that must be swapped
    elif sorted(a) == sorted(b):
        counter = 0
        similar = True
        for i in range(len(a)):
            if a[i] != b[i]:
                counter += 1
                if counter > 2:
                    similar = False

    return similar

a = [2, 3, 1]
b = [1, 3, 2]
print(are_similar(a, b))


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
