def binarySearch(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1
    middle_pointer = (left_pointer + right_pointer) // 2

    while left_pointer <= right_pointer:
        element = array[middle_pointer]

        if element == target:
            return middle_pointer
        elif element > target:
            right_pointer = middle_pointer - 1
            middle_pointer = (left_pointer + right_pointer) // 2
        else:
            left_pointer = middle_pointer + 1
            middle_pointer = (left_pointer + right_pointer) // 2

    return -1


def binarySearch(array, target):
    return recurse_binary_search(array, target, 0, len(array) - 1)


def recurse_binary_search(array, target, left_pointer, right_pointer):
    if left_pointer > right_pointer:
        return -1

    middle_pointer = (left_pointer + right_pointer) // 2
    element = array[middle_pointer]
    if element == target:
        return middle_pointer
    elif element > target:
        right_pointer = middle_pointer - 1
        return recurse_binary_search(array, target, left_pointer, right_pointer)
    else:
        left_pointer = middle_pointer + 1
        return recurse_binary_search(array, target, left_pointer, right_pointer)


def test():
    assert binarySearch([1, 2, 3], 3) == 2
    assert binarySearch([1, 2, 3], 2) == 1
    assert binarySearch([1, 2, 3], 1) == 0
    assert binarySearch([1, 2, 3], 0) == -1
    assert binarySearch([1, 2], 0) == -1
    assert binarySearch([1, 2], 1) == 0
    assert binarySearch([1, 2], 2) == 1
    assert binarySearch([], 0) == -1


if __name__ == "__main__":
    test()
