def mergeSort(array):
    if len(array) in (0, 1):
        return array

    middle = len(array) // 2
    left_array = mergeSort(array[:middle])
    right_array = mergeSort(array[middle:])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    total_length = len(left_array) + len(right_array)
    res = [None] * total_length

    i = 0
    j = 0
    k = 0

    while i < len(left_array) and j < len(right_array):
        left_el = left_array[i]
        right_el = right_array[j]

        if left_el <= right_el:
            res[k] = left_el
            i += 1
        else:
            res[k] = right_el
            j += 1

        k += 1

    while i < len(left_array):
        res[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        res[k] = right_array[j]
        j += 1
        k += 1

    return res
