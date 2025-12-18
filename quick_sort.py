import random


def quickSort(array):
    # NOTE: The easiest implementation in O(n) space.
    if len(array) in (0, 1):
        return array

    pivot = random.choice(array)
    less_than_pivot = [el for el in array if el < pivot]
    equal_to_pivot = [el for el in array if el == pivot]
    more_than_pivot = [el for el in array if el > pivot]

    return quickSort(less_than_pivot) + equal_to_pivot + quickSort(more_than_pivot)


def quickSort(array):
    # NOTE: Hard implementation in O(log n) space if you account for call stack.
    # Example: [8, 5, 2, 9, 5, 6, 3].
    # After the first "sorting": [6, 5, 2, 3, 5, (8), 9].
    return quickSortImpl(array, 0, len(array) - 1)


def quickSortImpl(array, left_index, right_index):
    if left_index >= right_index:
        return array

    pivot = array[left_index]
    left_pointer = left_index + 1
    right_pointer = right_index

    while left_pointer <= right_pointer:
        left_item = array[left_pointer]
        right_item = array[right_pointer]

        if left_item > pivot and right_item < pivot:
            array[left_pointer], array[right_pointer] = (
                array[right_pointer],
                array[left_pointer],
            )
            left_pointer += 1
            right_pointer -= 1
        elif left_item <= pivot:
            left_pointer += 1
        elif right_item >= pivot:
            right_pointer -= 1

    # NOTE: At this point right_pointer > left_pointer,
    # So it points to a number which is less than or equal to pivot.
    # Because of this, we can safely swap them and preserve the algorithm invariant.
    array[left_index], array[right_pointer] = array[right_pointer], array[left_index]

    left_size = (right_pointer - 1) - left_index
    right_size = right_index - (right_pointer + 1)

    # NOTE: It is suggested that we should recurse on the smallest subarray first.
    # I don't know why yet.
    # It has to do something with Space Complexity; Tail Recursion?
    if left_size > right_size:
        # NOTE: Right part is to be sorted first.
        quickSortImpl(array, right_pointer + 1, right_index)
        quickSortImpl(array, left_index, right_pointer - 1)
    else:
        # NOTE: Left part is to be sorted first.
        quickSortImpl(array, left_index, right_pointer - 1)
        quickSortImpl(array, right_pointer + 1, right_index)

    return array


def test():
    # print(quickSort([8, 5, 2, 9, 5, 6, 3]))
    print(quickSort([2, 1]))


if __name__ == "__main__":
    test()
