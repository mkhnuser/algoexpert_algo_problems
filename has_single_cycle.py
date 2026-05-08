def hasSingleCycle(array):
    # NOTE: array = [2, 3, 1, -4, -4, 2].    n = 6.
    #                0  1  2   3   4  5

    if not array:
        return True

    n = len(array)
    all_indices = set(i for i in range(0, n))
    visited_indices = set()
    i = 0

    while True:
        if i in visited_indices:
            # NOTE: A cycle which does not return back to the first element.
            return False

        el = array[i % n]
        visited_indices.add(i % n)
        i += el
        i %= n

        if i == 0:
            # NOTE: We are back at the first element.
            if visited_indices != all_indices:
                return False
            return True


def test():
    array = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycle(array))
    array = [-1, -1]
    print(hasSingleCycle(array))
    array = [1, -1]
    print(hasSingleCycle(array))
    array = [1, 1]
    print(hasSingleCycle(array))
    array = [-1, 1]
    print(hasSingleCycle(array))


if __name__ == "__main__":
    test()
