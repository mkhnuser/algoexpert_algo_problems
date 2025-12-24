def firstDuplicateValue(array):
    # NOTE: [2, 1, 5, 2, 3, 3, 4].
    seen = set()

    for num in array:
        if num in seen:
            return num
        seen.add(num)

    return -1


def firstDuplicateValue(array):
    # NOTE: [2, 1, 5, 2, 3, 3, 4].
    min_index = len(array)

    for i in range(len(array) - 1):
        el = array[i]
        for j in range(i + 1, len(array)):
            contender = array[j]
            if contender == el:
                min_index = min(min_index, j)

    return array[min_index] if min_index != len(array) else -1
