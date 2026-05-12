def smallestDifference(arrayOne, arrayTwo):
    min_abs_diff = float("+inf")
    first = None
    second = None
    for one in arrayOne:
        for two in arrayTwo:
            abs_diff = abs(one - two)
            if abs_diff < min_abs_diff:
                min_abs_diff = abs_diff
                first = one
                second = two

    return [first, second]


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    min_abs_diff = float("+inf")
    output = [None, None]

    # [-1, 3, 5, 10, 20, 28]
    # [15, 17, 26, 134, 135]

    i = 0
    j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        # NOTE: While both pointers are within bounds of both arrays.
        one = arrayOne[i]
        two = arrayTwo[j]
        abs_diff = abs(one - two)

        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
            output[0] = one
            output[1] = two

        if one == two:
            return output
        elif one < two:
            i += 1
        else:
            j += 1

    return output


def test():
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    print(smallestDifference(arrayOne, arrayTwo))


if __name__ == "__main__":
    test()
