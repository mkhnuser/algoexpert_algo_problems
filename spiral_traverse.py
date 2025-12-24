def spiralTraverse(array):
    output = []
    s_r = 0
    e_r = len(array) - 1
    s_c = 0
    e_c = len(array[0]) - 1

    while s_r <= e_r and s_c <= e_c:
        populate_for_boundries(array, output, s_r, e_r, s_c, e_c)
        s_r += 1
        e_r -= 1
        s_c += 1
        e_c -= 1

    return output


def populate_for_boundries(array, output, s_r, e_r, s_c, e_c):
    for c in range(s_c, e_c + 1):
        output.append(array[s_r][c])
    for r in range(s_r + 1, e_r + 1):
        output.append(array[r][e_c])
    if s_r < e_r:
        for c in range(e_c - 1, s_c, -1):
            output.append(array[e_r][c])
    if s_c < e_c:
        for r in range(e_r, s_r, -1):
            output.append(array[r][s_c])


def spiralTraverse(array):
    output = []
    s_r = 0
    e_r = len(array) - 1
    s_c = 0
    e_c = len(array[0]) - 1

    return spiralTraverseRecursive(array, output, s_r, e_r, s_c, e_c)


def spiralTraverseRecursive(array, output, s_r, e_r, s_c, e_c):
    if s_r > e_r or s_c > e_c:
        return output

    for c in range(s_c, e_c + 1):
        output.append(array[s_r][c])
    for r in range(s_r + 1, e_r + 1):
        output.append(array[r][e_c])
    if s_r < e_r:
        for c in range(e_c - 1, s_c, -1):
            output.append(array[e_r][c])
    if s_c < e_c:
        for r in range(e_r, s_r, -1):
            output.append(array[r][s_c])

    return spiralTraverseRecursive(array, output, s_r + 1, e_r - 1, s_c + 1, e_c - 1)


def test():
    array = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    spiralled = spiralTraverse(array)
    print(spiralled)
    array = [
        [1, 2, 3],
        [12, 13, 4],
        [11, 14, 5],
        [10, 15, 6],
        [9, 8, 7],
    ]
    spiralled = spiralTraverse(array)
    print(spiralled)

    array = [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6],
    ]
    spiralled = spiralTraverse(array)
    print(spiralled)


if __name__ == "__main__":
    test()
