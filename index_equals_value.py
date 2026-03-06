def indexEqualsValue(array):
    for i, value in enumerate(array):
        if i == value:
            return i
    return -1


def indexEqualsValue(array):
    ans = -1

    if not array:
        return ans

    indexes = list(range(len(array)))
    left_index = 0
    right_index = indexes[-1]

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if middle_index == array[middle_index]:
            ans = middle_index
            right_index = middle_index - 1
        elif middle_index < array[middle_index]:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    return ans


def test():
    assert indexEqualsValue([-5, -3, 0, 3, 4, 5, 9]) == 3
    assert indexEqualsValue([-5, -3, 2, 3, 4, 5, 9]) == 2
    assert indexEqualsValue([-5, -3, 2, 5, 6, 7, 8]) == 2
    #                       [ 0,  1, 2, 3, 4, 5, 6]

    assert indexEqualsValue([]) == -1
    assert indexEqualsValue([999]) == -1


if __name__ == "__main__":
    test()
