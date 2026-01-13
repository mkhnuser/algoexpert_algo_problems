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


def shiftedBinarySearch(array, target):
    return recurse_broken_search(array, target, 0, len(array) - 1)


def recurse_broken_search(nums, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    candidate = nums[middle]
    left_number = nums[left]
    right_number = nums[right]

    if candidate == target:
        return middle

    # NOTE: The key observation is that once you divide a shifted array into two halves,
    # one of the halves is always sorted.
    if left_number <= candidate:
        if target < candidate and target >= left_number:
            # NOTE: left_number <= candidate and target < candidate and target >= left_number.
            return recurse_broken_search(nums, target, left, middle - 1)
        else:
            # NOTE: left_number <= candidate and (target >= candidate or target < left_number).
            return recurse_broken_search(nums, target, middle + 1, right)
    else:
        if target > candidate and target <= right_number:
            # NOTE: left_number > candidate and target > candidate and target <= right_number.
            return recurse_broken_search(nums, target, middle + 1, right)
        else:
            # NOTE: left_number > candidate and (target <= candidate or target > right_number).
            return recurse_broken_search(nums, target, left, middle - 1)


def shiftedBinarySearch(array, target):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        candidate = array[middle_index]

        if candidate == target:
            return middle_index

        leftmost_item = array[left_index]
        rightmost_item = array[right_index]

        # NOTE: The key observation is that when you split an array into two halves,
        # one of them is guaraneed to be sorted.
        if leftmost_item < candidate:
            if target >= leftmost_item and target < candidate:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        else:
            if target > candidate and target <= rightmost_item:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1

    return -1


def test():
    assert shiftedBinarySearch([4, 1, 2, 3], 3) == 3
    assert shiftedBinarySearch([2, 3, 4, 1], 3) == 1
    assert shiftedBinarySearch([111, 1, 5, 23], 5) == 2
    assert shiftedBinarySearch([111, 1, 5, 23], 55) == -1
    assert shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33) == 8
    assert shiftedBinarySearch([19, 21, 100, 101, 1, 4, 5, 7, 12], 5) == 6


if __name__ == "__main__":
    test()
