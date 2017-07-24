"""1-9 longest string:
Given an array of strings, return another array containing all of its longest strings.

1-10 common chars:
Given two strings, find the number of common characters between them.

1-11 is lucky:
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half
of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not."""


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

a = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
print(all_longest_strings(a))


def common_character_count(s1, s2):
    """Input: A string consisting of lowercase latin letters a-z.
    Guaranteed constraints for both input strings: 1 ≤ str.length ≤ 15.
    Output: Returns the number of common characters between the two input strings."""
    counter = 0
    # sorting improves efficiency when looping
    sort1 = sorted(s1)
    sort2 = sorted(s2)

    for i in range(len(sort1)):
        s = sort1[i]
        j = 0
        while len(sort2) != 0 and s >= sort2[j]:
            if s == sort2[j]:
                counter += 1
                sort2.remove(s)    # to avoid duplicate matching
                break
            j += 1

    return counter

s1 = "abcaeeeeeee"
s2 = "abc"
print(common_character_count(s1, s2))


def is_lucky_long_version(n):
    """Input: A ticket number represented as a positive integer with an even number of digits.
    Guaranteed constraints: 10 ≤ n < 10**6.
    Output: Returns true if the sum of the first half of the digits equals the sum of the second."""
    #n_list = list(map(int, (str(n))))
    n_list = [int(x) for x in str(n)]

    half_n_len = int(len(n_list)/2)

    left_half = n_list[:half_n_len]
    right_half = n_list[half_n_len:]

    lucky = False

    if sum(left_half) == sum(right_half):
        lucky = True

    return lucky


def is_lucky_short_version(n):
    """Shorter version of the above"""
    l = [int(x) for x in str(n)]
    h = int(len(l)/2)

    return sum(l[:h]) == sum(l[h:])

n = 261534
print(is_lucky_short_version(n))
