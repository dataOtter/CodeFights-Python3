"""Find the area of an n-interesting polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1.
An n-interesting polygon is obtained by taking the (n-1)-interesting polygon
and appending 1-interesting polygons to its rim, side by side."""


def shape_area(n):
    """Input: Guaranteed constraints: 1 ≤ n < 10**4.
    Output: Returns the area of an n-interesting polygon for the given n."""
    area = (2*n*n) - (2*n) + 1
    return area

