"""After becoming famous, CodeBots decided to move to a new building and live together.
The building is represented by a rectangular matrix of rooms,
each cell containing an integer - the price of the room.
Some rooms are free (their cost is 0), but that's probably because they are haunted,
so all the bots are afraid of them. That is why any room that is free
or is located anywhere below a free room in the same column is not considered suitable for the bots.
Help the bots calculate the total price of all the rooms that are suitable for them."""


def matrixElementsSum(matrix):
    """Input: 2-dimensional array of integers representing a rectangular matrix of the building.
    Guaranteed constraints: 1 ≤ matrix.length ≤ 5, 1 ≤ matrix[i].length ≤ 5, 0 ≤ matrix[i][j] ≤ 10.
    Output: Returns the sum (total price) of all eligible room prices."""

    # Between 1 and 5 rows
    # Between 1 and 5 columns/entries per row
    # Max value of entry is 10, min 0

    total_price = 0
    prev_indices_to_avoid = []
    indices_to_avoid = []
    to_subtract = 0

    for row_index in range(len(matrix)):
        total_price += sum(matrix[row_index])
        print(prev_indices_to_avoid)

        for index, element in enumerate(matrix[row_index]):
            if element == 0:
                print(index)
                indices_to_avoid.append(index)

        prev_indices_to_avoid = indices_to_avoid.copy()
        indices_to_avoid.clear()

    print(total_price)


matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

matrixElementsSum(matrix)

