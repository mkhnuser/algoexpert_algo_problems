def moveElementToEnd(array, toMove):
    array.sort(key=lambda x: x if x != toMove else float("+inf"))
    return array


def moveElementToEnd(array, toMove):
    n = len(array)
    i = 0
    j = len(array) - 1

    while i < n:
        while array[i] == toMove and i < j:
            array[i], array[j] = array[j], array[i]
            j -= 1
        i += 1
    return array


def test():
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    print(moveElementToEnd(array, toMove))


if __name__ == "__main__":
    test()
