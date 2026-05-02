def shiftedBinarySearch(array, target):
    return recurse_shifted_binary_search(
        array=array,
        target=target,
        lower_index=0,
        upper_index=len(array) - 1,
    )


def recurse_shifted_binary_search(array, target, lower_index, upper_index):
    # NOTE: [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
    # target = 33 => output: 8.

    if lower_index > upper_index:
        return -1

    leftmost_element = array[0]
    middle_index = (lower_index + upper_index) // 2
    middle_element = array[middle_index]

    if middle_element == target:
        return middle_index
    elif middle_element > leftmost_element:  # NOTE: We are in a bigger part.
        if target < middle_element and target >= leftmost_element:
            return recurse_shifted_binary_search(
                array=array,
                target=target,
                lower_index=lower_index,
                upper_index=middle_index - 1,
            )
        return recurse_shifted_binary_search(
            array=array,
            target=target,
            lower_index=middle_index + 1,
            upper_index=upper_index,
        )
    else:  # NOTE: middle_element <= leftmost_element - a lower part.
        if target > middle_element and target < leftmost_element:
            return recurse_shifted_binary_search(
                array=array,
                target=target,
                lower_index=middle_index + 1,
                upper_index=upper_index,
            )
        return recurse_shifted_binary_search(
            array=array,
            target=target,
            lower_index=lower_index,
            upper_index=middle_index - 1,
        )
