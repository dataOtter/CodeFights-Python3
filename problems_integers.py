"""1. rounder:
We want to turn the given integer into a number that has only one non-zero digit
using a tail rounding approach. This means that at each step we take the last
non 0 digit of the number and round it to 0 or to 10. If it's less than 5
we round it to 0 if it's larger than or equal to 5 we round it to 10
(rounding to 10 means increasing the next significant digit by 1).
The process stops immediately once there is only one non-zero digit left."""


def rounders(value):
    """Input: positive integer value. Guaranteed constraints: 1 ≤ value ≤ 108.
    Output: Returns integer, the rounded number."""
    l = list(str(value))
    i = len(l) - 1
    while i > 0:
        if int(l[i]) >= 5:
            l[i - 1] = str(int(l[i - 1]) + 1)
        l[i] = '0'
        i -= 1
    v = ''.join(l)
    return v

value = 1445
print(rounders(value))
