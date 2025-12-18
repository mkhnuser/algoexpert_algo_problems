# NOTE: This is crazy solution. It works though.
def shiftedBinarySearch(array, target):
    n = len(array)
    left_pointer = 0
    right_pointer = n - 1

    # NOTE: We defensively check that the array indeed has a shift.
    # If it does not, we just apply binary search.

    turning_point_index = find_turning_point_index_recursively(
        array,
        n,
        left_pointer,
        right_pointer,
    )
    assert turning_point_index is not None

    if array[turning_point_index] == target:
        return turning_point_index

    left = binarySearch(array[0 : turning_point_index + 1], target)
    if left is not None:
        return left
    else:
        right = binarySearch(array[turning_point_index + 1 :], target)
        if right is not None:
            return turning_point_index + right + 1

    return -1


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

    return None


def find_turning_point_index_recursively(array, n, left_pointer, right_pointer):
    if left_pointer > right_pointer:
        return None

    middle_pointer = (left_pointer + right_pointer) // 2

    candidate = array[middle_pointer]
    l = (middle_pointer - 1) % n
    r = (middle_pointer + 1) % n

    element_to_the_left = array[l]
    element_to_the_right = array[r]

    # NOTE: [1, 2, 3, 4] normal array.
    # NOTE: [4, 1, 2, 3] right shift 1.
    # NOTE: [2, 3, 4, 1] left shift 1.
    if element_to_the_left > candidate and element_to_the_right > candidate:
        return middle_pointer
    else:
        # NOTE: This is not O(logn).
        left_sub_array_turning_point_index = find_turning_point_index_recursively(
            array,
            n,
            left_pointer,
            middle_pointer - 1,
        )
        if left_sub_array_turning_point_index is not None:
            return left_sub_array_turning_point_index

        right_sub_array_turning_point_index = find_turning_point_index_recursively(
            array,
            n,
            middle_pointer + 1,
            right_pointer,
        )
        return right_sub_array_turning_point_index


### NOTE: Solution number 1 ends here.


def test():
    assert shiftedBinarySearch([4, 1, 2, 3], 3) == 3
    assert shiftedBinarySearch([2, 3, 4, 1], 3) == 1
    assert shiftedBinarySearch([111, 1, 5, 23], 5) == 2
    assert shiftedBinarySearch([111, 1, 5, 23], 55) == -1


if __name__ == "__main__":
    test()
