"""Given two strings, find the number of common characters between them."""


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

