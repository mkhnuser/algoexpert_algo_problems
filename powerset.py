def powerset(array):
    # NOTE: array = [1, 2] => [[], [1], [2], [1, 2]].
    # NOTE: array = [1, 2, 3] => [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]].
    output = []
    output.append([])

    for number in array:
        new_subsets = []
        for subset in output:
            new_subset = []
            new_subset.extend(subset)
            new_subset.append(number)
            new_subsets.append(new_subset)
        output.extend(new_subsets)

    return output


def powerset(array):
    return recurse_powerset(array)


def recurse_powerset(array):
    pass


def test():
    # assert powerset([]) == [[]]
    # assert powerset([1, 2]) == [[], [1], [2], [1, 2]]
    assert powerset([1, 2, 3]) == [
        [],
        [1],
        [2],
        [3],
        [1, 2],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]


if __name__ == "__main__":
    test()
