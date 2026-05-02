import heapq


def findThreeLargestNumbers(array):
    return find_three_largest_numbers(array)


def find_three_largest_numbers(array):
    return sorted(heapq.nlargest(n=3, iterable=array))
