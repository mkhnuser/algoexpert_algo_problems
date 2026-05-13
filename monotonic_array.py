def isMonotonic(array):
    if len(array) in (0, 1):
        return True

    return is_non_decreasing(array) or is_non_increasing(array)


def is_non_decreasing(array):
    for i in range(1, len(array)):
        current_element = array[i]
        prev_element = array[i - 1]
        if current_element - prev_element < 0:
            return False
    return True


def is_non_increasing(array):
    for i in range(1, len(array)):
        current_element = array[i]
        prev_element = array[i - 1]
        if current_element - prev_element > 0:
            return False
    return True
