"""
Chapter2 of grokking algorithms.
"""


def find_smallest_number(arr):
    """
    Find the smallest element in an array
    :param arr: input array
    :return: index of the smallest element
    """
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    Loops through the array and returns sorted array
    :param arr: input array
    :return: sorted array
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest_number(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
