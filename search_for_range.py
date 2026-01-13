def searchForRange(array, target):
    return [find_first_index(array, target), find_last_index(array, target)]


def find_first_index(array, target):
    ans = -1
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if array[middle_index] == target:
            ans = middle_index
            right_index = middle_index - 1
        elif array[middle_index] > target:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    return ans


def find_last_index(array, target):
    ans = -1
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if array[middle_index] == target:
            ans = middle_index
            left_index = middle_index + 1
        elif array[middle_index] > target:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    return ans


def test():
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    assert find_first_index(array, 45) == 4
    assert find_last_index(array, 45) == 9
    assert searchForRange(array, 45) == [4, 9]
    assert searchForRange(array, 46) == [-1, -1]


if __name__ == "__main__":
    test()
