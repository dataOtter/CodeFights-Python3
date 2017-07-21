"""Given two strings, find the number of common characters between them."""


def common_character_count(s1, s2):
    """Input: A string consisting of lowercase latin letters a-z.
    Guaranteed constraints for both input strings: 1 ≤ str.length ≤ 15.
    Output: Returns the number of common characters between the two input strings."""
    counter = 0
    s1_list = list(s1)
    s2_list = list(s2)

    for element in s1_list:
        if element in s2_list: # function to compare elements from sorted list i.e. a<b
            counter += 1
            s2_list.remove(element)
            #print(s2_list)

    return counter


s1 = "abca"
s2 = "xyzbac"
print(common_character_count(s1, s2))

print('a'<'b')

