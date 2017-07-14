"""Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue
will be bigger than the previous one exactly by 1.
He may need some additional statues to be able to accomplish that.
Help him figure out the minimum number of additional statues needed."""


def make_array_consecutive(statues):
    """Input: An array of distinct non-negative integers.
    Guaranteed constraints: 1 ≤ statues.length ≤ 10, 0 ≤ statues[i] ≤ 20.
    Output: Returns the number of statues to be added to fulfill the above task."""
    statues_ordered = sorted(statues)
    statues_to_add = 0

    for statue_index in range(len(statues_ordered)-1):
        current_statue = statues_ordered[statue_index]
        next_statue = statues_ordered[statue_index + 1]
        # if next_statue is equal to current_statue + 1, no statues need to be added
        statues_to_add += next_statue - current_statue - 1

    return statues_to_add
