def isMonotonic(array):
    if len(array) in (0, 1):
        return True

    return is_non_increasing(array) or is_non_decreasing(array)


def is_non_increasing(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True


def is_non_decreasing(array):
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            return False
    return True
