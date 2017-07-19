"""Given an array of strings, return another array containing all of its longest strings."""


def all_longest_strings(input_array):
    """Input: A non-empty array. Guaranteed constraints:
    1 ≤ inputArray.length ≤ 10, 1 ≤ inputArray[i].length ≤ 10.
    Output: Returns an array of all longest strings from the input array."""
    longest_length = 0
    longest_strings = []

    for element in input_array:
        length = len(element)

        if length == longest_length:
            longest_strings.append(element)

        elif length > longest_length:
            longest_strings.clear()
            longest_strings.append(element)
            longest_length = length

    return longest_strings


a = ["a",
 "abc",
 "cbd",
 "zzzzzz",
 "a",
 "abcdef",
 "asasa",
 "aaaaaa"]
print(allLongestStrings(a))