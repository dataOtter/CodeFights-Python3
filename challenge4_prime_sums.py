"""Return the number of ways to write the given n as the sum of two prime numbers."""



def gold(n):
    """Input: integer n. Guaranteed Constraints: 2 ≤ n ≤ 10**5.
    Output: Returns the number of ways to write n as the sum of two prime numbers"""
    counter = 0
    primes = get_primes(n)
    for i in range((n//2)+1):
        if primes[i] and primes[n-i]:
            counter += 1

    return counter


def get_primes(num):
    is_true = []
    for n in range(num):
        is_true.append(True)
    is_true[0] = is_true[1] = False
    i = 2
    for i in range(2, num//i):
        if is_true[i]:
            p = i*2
            while p < num:
                is_true[p] = False
                p += i
    return is_true

print(gold(4))

