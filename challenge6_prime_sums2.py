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
    p = get_powers()
    l = 1
    if n == 0:
        return 0
    while not check_len(n, p, l):
        l += 1
    return l


def check_len(n, p, lev):
    if lev == 1:
        return check_len1(n, p)
    else:
        for i in p:
            if check_len(n-i, p, lev-1):
                    return True


def check_len1(n, p):
    for i in p:
        if n == i:
            return True
    return False


def get_powers():
    powers = [1]
    for i in range(2, 10):
        for j in range(1, 10):
            powers.append(i**j)
    return sorted(set(powers))


'''def best_base(n):
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

    return [base, y]'''

print(raiseItMinLength(7221))
