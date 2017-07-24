"""1-1 add:
Write a function that returns the sum of two numbers.

1-2 century:
Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100,
the second from the year 101 up to and including the year 200, etc.

1-3 palindrome:
Given a string, check if it is a palindrome."""
import math


def add(param1, param2):
    """Input: Guaranteed constraints for integers param1 and param2: -100 ≤ param ≤ 1000.
    Output: Returns the sum of the two given numbers"""
    result = int(param1) + int(param2)
    return result


def century_from_year(year):
    """Input: A positive integer, designating the year.
    Output: Returns the century of the given year."""
    century = math.ceil(year/100)
    return century


def check_palindrome(input_string):
    """Input: A non-empty string consisting of lowercase characters.
    Output: Returns True if the input string is a palindrome."""
    string_reversed = input_string[::-1]
    if string_reversed == input_string:
        palindrome = True
    else:
        palindrome = False
    return palindrome
