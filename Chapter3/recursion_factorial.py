"""Recursion Exercises"""


def factorial(number):
    """
    Calculate factorial of a number
    :param number: input number
    :return: factorial of the number
    """
    if number == 1:
        return 1
    return number * factorial(number - 1)
