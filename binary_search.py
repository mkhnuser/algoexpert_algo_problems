def binarySearch(array, target):
    return recurse_binary_search(
        array=array,
        target=target,
        lower_index=0,
        higher_index=len(array) - 1,
    )


def recurse_binary_search(array, target, lower_index, higher_index):
    if lower_index > higher_index:
        return -1

    middle_index = (lower_index + higher_index) // 2
    current_element = array[middle_index]

    if current_element == target:
        return middle_index
    elif current_element < target:
        return recurse_binary_search(
            array=array,
            target=target,
            lower_index=middle_index + 1,
            higher_index=higher_index,
        )
    else:
        return recurse_binary_search(
            array=array,
            target=target,
            lower_index=lower_index,
            higher_index=middle_index - 1,
        )
