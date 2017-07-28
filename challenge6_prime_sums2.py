"""There was a recent reverse challenge called raiseIt, the algorithm of which takes
an array of two digit numbers and finds the sum of the first digit raised to the power
of the second digit. For example raiseIt([20, 42]) = 20 + 42 = 1 + 16 = 17.
In that task, I was curious what the shortest array would be that generated the largest
possible output. In this new task, now I'm curious about what the length of the shortest
array for any given number is.
Given an integer n, find the length of the shortest array arr such that raiseIt(arr) = n."""
import math as m


def raiseItMinLength(n):
    """Input: integer n. Guaranteed constraints: 0 ≤ n ≤ 10**5.
    Output: integer. The length of the shortest array arr such that raiseIt(arr) = n."""
    if n == 0:
        return 0

    a_len = 0
    a = best_base(n)

    while a[0]**a[1] != n:
        print(a)
        n -= (a[0]**a[1])
        a = best_base(n)
        a_len += 1

    return a_len


def best_base(n):
    dec = 1
    for b in range(2, 10):
        exp = m.log(n, b)
        ydec = exp % 1
        if ydec == 0:
            base, y = b, exp
            break
        elif ydec < dec:
            dec = ydec
            base, y = b, int(exp)

    return [base, y]

print(raiseItMinLength(16))
