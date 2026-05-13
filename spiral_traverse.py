def spiralTraverse(array):
    r_s = 0
    r_e = len(array) - 1
    c_s = 0
    c_e = len(array[0]) - 1

    output = []

    while r_s <= r_e and c_s <= c_e:
        # NOTE: The top-first row.
        for i in range(c_s, c_e + 1):
            output.append(array[r_s][i])

        # NOTE: Right.
        for i in range(r_s + 1, r_e + 1):
            output.append(array[i][c_e])

        if r_s != r_e:
            # NOTE: Bottom.
            for i in reversed(range(c_s + 1, c_e)):
                output.append(array[r_e][i])

        if c_s != c_e:
            # NOTE: Left.
            for i in reversed(range(r_s + 1, r_e + 1)):
                output.append(array[i][c_s])

        r_s += 1
        r_e -= 1
        c_s += 1
        c_e -= 1

    return output


def test():
    matrix = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    print(spiralTraverse(matrix))


if __name__ == "__main__":
    test()
