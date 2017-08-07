"""This is a reverse challenge, enjoy!"""


def build_sum(n):
    """Input: integer n. Guaranteed constraints: 0 ≤ n < 10.
    Output: Integer = 1 + sum{j=1..n} j**j"""
    result = 0
    for i in range(n+1):
        result += i**i
    return result

print(build_sum(3))


def build_sum2(n):
    return sum(x**x for x in range(n+1))

print(build_sum2(3))
