"""Given a rectangular matrix of characters, add a border of asterisks(*) to it."""


def addBorder(picture):
    """Input: array.string picture. A non-empty array of non-empty equal-length strings.
    Guaranteed constraints: 1 ≤ picture.length ≤ 5, 1 ≤ picture[i].length ≤ 5.
    Output: Returns array.string, the same matrix of characters, framed with a border of asterisks of width 1."""
    width = len(picture[0]) + 2
    for i in range(len(picture)):
        new_s = picture[i][0]




    #picture.insert(0, )