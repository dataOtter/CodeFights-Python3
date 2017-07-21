"""CodeFights programming problems 1- from Arcade-Core."""


def add_two_digits(n):
    """Input: A positive two-digit integer. Guaranteed constraints: 10 ≤ n ≤ 99.
    Output: Returns the sum of first and second digits of the integer."""
    return n % 10 + n//10


def largest_number(n):
    """Input: Integer n. Guaranteed constraints: 1 ≤ n ≤ 7.
    Output: Returns the largest integer that contains exactly n digits."""
    list_str = ['9'] * n
    to_str = ''.join(list_str)
    return int(to_str)


def candies(n, m):
    """n children have got m pieces of candy. They want to eat as much candy as they can,
    but each child must eat exactly the same amount of candy as any other child.
    Determine how many pieces of candy will be eaten by all the children together.
    Individual pieces of candy cannot be split.
    Input: Integer n. The number of children. Guaranteed constraints: 1 ≤ n ≤ 10.
    Integer m. The number of pieces of candy. Guaranteed constraints: 2 ≤ m ≤ 100.
    Output: Returns and integer of the total number of pieces of candy the children will eat."""
    return m - (m % n)


