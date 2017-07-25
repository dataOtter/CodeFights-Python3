"""A reverse challenge is a special type of challenge, where no description is provided!
You have to solve two challenges in one: find out what the author wants from you and write a solution.
Check out this page for more information."""


def raise_it(arg):
    """Input: array.integer arg1. Guaranteed constraints: 0 ≤ arg1.length ≤ 4 · 10**4, 10 ≤ arg1[i] ≤ 99.
    Output: Returns an integer. Guaranteed constraints: 0 ≤ output ≤ 231 - 1."""
    '''result = 0
    for num in arg:
        a = int(num / 10)
        b = num % 10
        result += a**b

    return result'''

    return sum(pow(int(n / 10), n % 10) for n in arg)

arg1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(raise_it(arg1))



