def indexEqualsValue(array):
    for i in range(len(array)):
        if i == array[i]:
            return i
    return -1


def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    indexes = []

    while left <= right:
        index = (left + right) // 2
        el = array[index]
        break

    return indexes[-1] if indexes else -1


def test():
    assert indexEqualsValue([-5, -3, 0, 3, 3, 3, 3, 3, 4, 5, 9]) == 3
    assert indexEqualsValue([0, 0, 0, 0, 0, 0]) == 0
    assert indexEqualsValue([]) == -1
    assert indexEqualsValue([-5, -4, -3]) == -1


if __name__ == "__main__":
    test()
