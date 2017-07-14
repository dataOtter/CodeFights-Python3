"""Given a string, check if it is a palindrome."""


def check_palindrome(input_string):
    """Input: A non-empty string consisting of lowercase characters.
    Output: Returns True if the input string is a palindrome."""
    string_reversed = input_string[::-1]

    if string_reversed == input_string:
        palindrome = True
    else:
        palindrome = False

    return palindrome
