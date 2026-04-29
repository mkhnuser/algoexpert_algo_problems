def getPermutations(array):
    if not array:
        return []
    return recurse(array)


def recurse(array):
    if len(array) == 0:
        return [[]]

    permutations = recurse(array[1:])
    res = []

    for p in permutations:
        for i in range(len(p) + 1):
            c = p.copy()
            c.insert(i, array[0])
            res.append(c)

    return res


def test():
    input = [1, 2, 3]
    output = getPermutations(input)
    print(output)


if __name__ == "__main__":
    test()
