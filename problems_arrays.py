"""1. Is smooth:
We define the middle of the array arr as follows:
    if arr contains an odd number of elements, its middle is the element whose index number
    is the same when counting from the beginning of the array and from its end;
    if arr contains an even number of elements, its middle is the sum of the two elements
    whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle.
Given an array arr, determine if it is smooth or not.

2. Are isomorphic:
Two two-dimensional arrays are isomorphic if they have the same number of rows
and each pair of respective rows contains the same number of elements.
Given two two-dimensional arrays, check if they are isomorphic.

3. 2D sorting:
Given an array of strings, produce a single string as follows:
Repeat the following steps while there is more than one string in the array:
    find the shortest string in the array (if there are several strings of the same length take the leftmost one);
    find the shortest string among the rest (if there are several strings of the same length take the rightmost one);
    extract the chosen strings from the array;
    append the result of their concatenation (the second string should be added
    to the end of the first string) to the right end of the array.
After the algorithm has finished, there will be a single string left in the array. Return that string."""


def is_smooth(arr):
    """Input: array.integer arr. Guaranteed constraints: 2 ≤ arr.length ≤ 10**5, -10**9 ≤ arr[i] ≤ 10**9.
    Output: Returns boolean true if arr is smooth, false otherwise."""
    l = len(arr)
    if l % 2 == 0:
        m = arr[(l // 2) - 1] + arr[(l // 2)]
    else:
        m = arr[l // 2]

    if arr[0] == arr[l - 1] and arr[0] == m:
        return True
    else:
        return False

arr = [7, 2, 2, 5, 10, 7]
print(is_smooth(arr))


def are_isomorphic(array1, array2):
    """Input: array.array.integer array1, array2. Guaranteed constraints:
    1 ≤ array.length ≤ 5, 0 ≤ array[i].length ≤ 5, 0 ≤ array1[i][j] ≤ 50.
    Output: Returns boolean true if the arrays are isomorphic, false otherwise."""
    answer = True
    if len(array1) != len(array2):
        answer = False
    else:
        for i in range(len(array1)):
            if len(array1[i]) != len(array2[i]):
                answer = False
                break

    return answer

array1 = [[1, 1, 1],
          [0, 0]]
array2 = [[2, 1, 1],
          [2, 1]]
print(are_isomorphic(array1, array2))


def concatenation_process(init):
    """Input: non-empty array.string init. Guaranteed constraints: 1 ≤ init.length ≤ 10, 0 ≤ init[i].length ≤ 25.
    Output: Returns the resulting single string."""
    shortest = [init[0]]
    shortest2 = []

    for string in init:
        if len(string) < len(shortest[0]):
            shortest2 = shortest.copy()
            shortest = [string]
        elif len(string) == len(shortest[0]):
            shortest.append(string)

    init.remove(shortest[0])
    init.remove(shortest2[0])
    s = ''.join(init) + shortest[0] + shortest2[len(shortest2)-1]

    return s

init = ["aaa", "dd", "bbbbb"]
print(concatenation_process(init))
