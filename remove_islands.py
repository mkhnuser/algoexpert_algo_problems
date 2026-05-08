from collections import deque


ISLAND_ITEM = 1
DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


def safen(i, j, safe_set, n, m, matrix):
    d = deque()
    d.append((i, j))

    while d:
        c = d.popleft()
        i, j = c

        if i < 0 or j < 0 or i >= n or j >= m:
            continue

        item = matrix[i][j]

        if item == 0:
            continue

        if (i, j) in safe_set:
            continue

        safe_set.add((i, j))

        for direction in DIRECTIONS:
            i_increment, j_increment = direction
            next_i = i + i_increment
            next_j = j + j_increment
            d.append((next_i, next_j))


def removeIslands(matrix):
    # NOTE: 1 = black, 0 = white.
    # Islands consists of 1s which don't touch the border of a matrix.
    # An objective: remove all islands by replacing them with zeroes.
    #
    # An algorithm:
    # Go over a matrix borders;
    # Mark islands which span from border as safe.
    # Remove all unsafe islands.

    n = len(matrix)
    m = len(matrix[0])
    safe_set = set()

    for i in (0, n - 1):
        for j in range(m):
            if matrix[i][j] == ISLAND_ITEM:
                safen(i, j, safe_set, n, m, matrix)

    for j in (0, m - 1):
        for i in range(n):
            if matrix[i][j] == ISLAND_ITEM:
                safen(i, j, safe_set, n, m, matrix)

    for i in range(n):
        for j in range(m):
            item = matrix[i][j]
            if item == ISLAND_ITEM and (i, j) not in safe_set:
                matrix[i][j] = 0

    return matrix


def test():
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    print(removeIslands(matrix))


if __name__ == "__main__":
    test()
