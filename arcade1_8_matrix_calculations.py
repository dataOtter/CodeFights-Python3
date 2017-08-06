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

    indices_to_sub = []    # array of column-wise locations of haunted rooms
    sum_price = sum(map(sum, matrix))    # total price of all rooms without subtractions

    # to look at each row in the matrix
    for row_index in range(len(matrix)):
        #print("current total: " + str(sum_price))
        #print(row_index, set(indices_to_sub))

        # for all column-wise locations of haunted rooms
        for column_index in indices_to_sub:
            # total price "minus" price of the room in that column-wise location in the current row
            sum_price -= matrix[row_index][column_index]

        # for every index (location), element (room) pair in the current row
        for index, element in enumerate(matrix[row_index]):
            # if the room is empty i.e. haunted and
            # this room's column-wise location is not already in the haunted room locations array
            # i.e. it is not below another haunted room
            if element == 0 and index not in indices_to_sub:
                # add that room's location to the list of locations of haunted rooms
                indices_to_sub.append(index)

    return sum_price


matrix = [[0]]

print(matrix_elements_sum(matrix))

