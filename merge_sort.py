def mergeSort(array):
    # NOTE: Child's play.
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


def mergeSort(array):
    # NOTE: Crazy.
    if len(array) <= 1:
        return array

    additional_array = array.copy()
    help_me(array, 0, len(array) - 1, additional_array)
    return array


def help_me(main_array, left_index, right_index, additional_array):
    if left_index == right_index:
        return

    # NOTE: Divide.
    middle_index = (left_index + right_index) // 2
    help_me(additional_array, left_index, middle_index, main_array)
    help_me(additional_array, middle_index + 1, right_index, main_array)

    # NOTE: Conquer.
    help_me_again(main_array, left_index, middle_index, right_index, additional_array)


def help_me_again(main_array, left_index, middle_index, right_index, additional_array):
    k = left_index
    i = left_index
    j = middle_index + 1

    while i <= middle_index and j <= right_index:
        if additional_array[i] <= additional_array[j]:
            main_array[k] = additional_array[i]
            i += 1
        else:
            main_array[k] = additional_array[j]
            j += 1

        k += 1

    while i <= middle_index:
        main_array[k] = additional_array[i]
        i += 1
        k += 1

    while j <= right_index:
        main_array[k] = additional_array[j]
        j += 1
        k += 1
