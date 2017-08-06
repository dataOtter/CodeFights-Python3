"""This is a reverse challenge, enjoy!"""


def list_to_string(l):
    """Input: array.integer l. An array of integers with length 3.
    Guaranteed constraints: l.length = 3, -10**5 ≤ l[i] ≤ 10**5.
    Output: Coverts the 3 list elements to base 8, 2, and 16, respectively.
    Negative signs ignored, integer treated as a positive number.
    Returns one string with negative sign replacing space between converted numbers."""
    l2 = [oct(abs(l[0]))[2:], bin(abs(l[1]))[2:], hex(abs(l[2]))[2:]]

    for i in range(3):
        if l[i] < 0:
            l2[i] = '-' + l2[i]
        else:
            l2[i] = ' ' + l2[i]

    return ''.join(l2).lstrip()

l = [10, 100, 1000]
ll = [-1, -1, -1]
print(list_to_string(ll))
