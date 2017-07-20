"""Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half
of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not."""


def is_lucky(n):
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


def is_lucky2(n):
    l = [int(x) for x in str(n)]
    h = int(len(l)/2)

    return sum(l[:h]) == sum(l[h:])


n = 261534
print(is_lucky2(n))
