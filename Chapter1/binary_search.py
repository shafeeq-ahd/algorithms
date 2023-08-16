"""
Chapter1 of grokking algorithms.
"""


def binary_search(input_array, item):
    """
    This function return the index of an item in a list
    :param input_array: array from which item needs to be searched
    :param item: item which needs to be searched in the list
    :return: index of the searched item
    """
    low = 0
    high = len(input_array) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = input_array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
