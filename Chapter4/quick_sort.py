""" Script for recursion quick sort"""


def quick_sort(arr):
    """
    Sort an array using quick sorting algorithm
    :param arr: input array
    :return: sorted array
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
