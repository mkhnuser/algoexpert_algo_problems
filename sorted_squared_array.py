def sortedSquaredArray(array):
    res = [num**2 for num in array]  # O (n)
    res.sort()  # O(n log n)
    return res


def sortedSquaredArray(array):
    result = []
    abs_array = [abs(num) for num in array]
    L = 0
    R = len(array) - 1

    while L <= R:
        left_abs_element = abs_array[L]
        right_abs_element = abs_array[R]

        if right_abs_element > left_abs_element:
            result.append(right_abs_element**2)
            R -= 1
        else:
            # right_abs_element < or = left_abs_element.
            result.append(left_abs_element**2)
            L += 1

    result.reverse()
    return result


def sortedSquaredArray(array):
    result = [None for _ in range(len(array))]

    i = len(array) - 1
    L = 0
    R = len(array) - 1

    while L <= R:
        left_abs_element = abs(array[L])
        right_abs_element = abs(array[R])

        if right_abs_element > left_abs_element:
            result[i] = right_abs_element**2
            R -= 1
        else:
            # right_abs_element < or = left_abs_element.
            result[i] = left_abs_element**2
            L += 1

        i -= 1

    return result


if __name__ == "__main__":
    print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
    print(sortedSquaredArray([-2, -1, 0, 3, 4]))
