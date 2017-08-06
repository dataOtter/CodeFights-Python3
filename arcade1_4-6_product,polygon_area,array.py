"""1-4 largest product:
Given an array of integers, find the pair of adjacent elements
that has the largest product and return that product.

1-5 polygon area:
Find the area of an n-interesting polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the (n-1)-interesting polygon
and appending 1-interesting polygons to its rim, side by side.

1-6 consecutive array:
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue
will be bigger than the previous one exactly by 1.
He may need some additional statues to be able to accomplish that.
Help him figure out the minimum number of additional statues needed.
"""


def adjacent_elements_product(input_array):
    """Input: An array of integers containing at least two elements.
    Output: Returns the largest product of all element pair products in the given array."""
    prev_element = input_array[0]
    biggest_product = -99999999

    for element in input_array[1:]:
        temp_product = prev_element*element

        if temp_product > biggest_product:
            biggest_product = temp_product
        prev_element = element

    return biggest_product


def shape_area(n):
    """Input: Guaranteed constraints: 1 ≤ n < 10**4.
    Output: Returns the area of an n-interesting polygon for the given n."""
    area = (2*n*n) - (2*n) + 1
    return area


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
