"""After becoming famous, CodeBots decided to move to a new building and live together.
The building is represented by a rectangular matrix of rooms,
each cell containing an integer - the price of the room.
Some rooms are free (their cost is 0), but that's probably because they are haunted,
so all the bots are afraid of them. That is why any room that is free
or is located anywhere below a free room in the same column is not considered suitable for the bots.
Help the bots calculate the total price of all the rooms that are suitable for them."""


def matrix_elements_sum(matrix):
    """Input: 2-dimensional array of integers representing a rectangular matrix of the building.
    Guaranteed constraints: 1 ≤ matrix.length ≤ 5, 1 ≤ matrix[i].length ≤ 5, 0 ≤ matrix[i][j] ≤ 10.
    Output: Returns the sum (total price) of all eligible room prices."""

    indices_to_sub = []
    sum_price = sum(map(sum, matrix))

    for row_index in range(len(matrix)):
        #print("current total: " + str(sum_price))
        #print(row_index, set(indices_to_sub))
        for column_index in indices_to_sub:
            sum_price -= matrix[row_index][column_index]

        for index, element in enumerate(matrix[row_index]):
            if element == 0 and index not in indices_to_sub:
                indices_to_sub.append(index)

    return sum_price


matrix = [[0]]

print(matrix_elements_sum(matrix))

