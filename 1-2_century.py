"""Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100,
the second from the year 101 up to and including the year 200, etc."""
import math


def century_from_year(year):
    """Input: A positive integer, designating the year.
    Output: Returns the century of the given year."""
    century = math.ceil(year/100)
    return century