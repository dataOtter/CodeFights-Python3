"""Given a sequence of integers as an array, determine
whether it is possible to obtain a strictly increasing sequence
by removing no more than one element from the array."""


def almost_increasing_sequence(sequence):
    """Input: Guaranteed constraints: 2 ≤ sequence.length ≤ 10**5, -10**5 ≤ sequence[i] ≤ 10**5.
    Output: Returns true if sequence is almost increasing."""
    index_a = find_first_violation(sequence)
    success = True

    if index_a != -1:
        without_a = sequence[:index_a] + sequence[index_a+1:]
        #print(without_a)

        if find_first_violation(without_a) != -1:
            without_b = sequence[:index_a+1] + sequence[index_a+2:]
            #print(without_b)

            if find_first_violation(without_b) != -1:
                success = False
    return success


def find_first_violation(seq):
    # Returns index of first violation, -1 otherwise.
    index = -1
    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            index = i
            break
    return index

