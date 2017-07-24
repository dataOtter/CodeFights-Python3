"""Given a string, find out if its characters can be rearranged to form a palindrome."""


def palindrome_rearranging(string_in):
    """Input: string string_in. A string consisting of lowercase English letters.
    Guaranteed constraints: 1 ≤ string_in.length ≤ 50.
    Output: Returns true if the characters of string_in can be rearranged to form a palindrome, false otherwise."""
    palindrome = False
    s_sort = sorted(string_in)    # # loop-count = 1
    # take every other character from the sorted array and put it into two new arrays (offset 1 for second array)
    s_left = s_sort[::2]    # loop-count = 2
    s_right = s_sort[1::2]    # loop-count = 3

    # even number of characters means all characters/letters have to exist an even number of times,
    # i.e. the arrays must be exactly equal
    if len(string_in) % 2 == 0:
        if s_right == s_left:    # loop???
            palindrome = True
    # odd number of characters means at most one character/letter can exist an odd number of times
    else:
        counter, i = 0, 0
        while i < len(s_right):    # loop-count = 4
            if counter > 1:
                return False
            if s_left[i] != s_right[i]:
                s_left.remove(s_left[i])    # loop???
                counter += 1
                continue
            i += 1
        palindrome = True

    return palindrome


def palindrome_rearranging2(string_in):
    """This alternative has shorter code, but the whole code is executed in every case."""
    s_list = list(string_in)    # loop-count = 1
    s_set = set(string_in)    # loop-count = 2
    counter = 0

    for x in s_set:    # loop-count = 3
        occurrences = s_list.count(x)    # loop-count = 3 + len(s_set)
        counter += occurrences % 2

    return counter <= 1

s = "abc"
print(palindrome_rearranging(s))
