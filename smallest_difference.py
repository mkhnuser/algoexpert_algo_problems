def smallestDifference(arrayOne, arrayTwo):
    min_abs_diff = float("+inf")
    output = [None, None]

    for num_one in arrayOne:
        for num_two in arrayTwo:
            diff = abs(num_one - num_two)
            if diff < min_abs_diff:
                min_abs_diff = diff
                output[0] = num_one
                output[1] = num_two

    return output


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    output = [None, None]
    min_abs_diff = float("+inf")

    pointer_one = 0
    pointer_two = 0

    while pointer_one < len(arrayOne) and pointer_two < len(arrayTwo):
        diff = abs(arrayOne[pointer_one] - arrayTwo[pointer_two])

        if diff < min_abs_diff:
            min_abs_diff = diff
            output[0] = arrayOne[pointer_one]
            output[1] = arrayTwo[pointer_two]

        if arrayOne[pointer_one] == arrayTwo[pointer_two]:
            return output
        elif arrayOne[pointer_one] < arrayTwo[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1

    return output


def test():
    print(
        smallestDifference(
            [-1, 5, 10, 20, 28, 3],
            [26, 134, 135, 15, 17],
        )
    )


if __name__ == "__main__":
    test()
