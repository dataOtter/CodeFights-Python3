"""Given an array of integers, find the pair of adjacent elements
that has the largest product and return that product."""


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
