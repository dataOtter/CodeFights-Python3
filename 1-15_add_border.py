"""Given a rectangular matrix of characters, add a border of asterisks(*) to it."""


def add_border(picture):
    """Input: array.string picture. A non-empty array of non-empty equal-length strings.
    Guaranteed constraints: 1 ≤ picture.length ≤ 5, 1 ≤ picture[i].length ≤ 5.
    Output: Returns array.string, the same matrix of characters, framed with a border of asterisks of width 1."""
    width = len(picture[0]) + 2
    border = ['*' * width]

    for s in picture:
        border.append("*" + s + "*")
    border.append(border[0])

    return border

picture = ["abc", "ded"]
print(add_border(picture))
