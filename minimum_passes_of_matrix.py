DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)


def can_be_negated(i, j, n, m, matrix):
    for direction in DIRECTIONS:
        i_incr, j_incr = direction
        next_i = i + i_incr
        next_j = j + j_incr

        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
            # NOTE: Ensure the cell is within the matrix.
            continue

        next_el = matrix[next_i][next_j]

        if next_el > 0:
            return True

    return False


def minimumPassesOfMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    counter = 0

    while True:
        to_be_negated_coords = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] < 0 and can_be_negated(i, j, n, m, matrix):
                    to_be_negated_coords.add((i, j))

        if not to_be_negated_coords:
            break

        for coord in to_be_negated_coords:
            i, j = coord
            matrix[i][j] *= -1

        counter += 1

    # NOTE: If there is some isolated neg. el., return -1.
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < 0:
                return -1

    return counter


def test():
    matrix = [
        [0, -2, -1],
        [-5, 2, 0],
        [-6, -2, 0],
    ]
    print(minimumPassesOfMatrix(matrix))

    matrix = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1],
    ]
    print(minimumPassesOfMatrix(matrix))

    matrix = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
    ]
    print(minimumPassesOfMatrix(matrix))

    matrix = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1],
    ]
    print(minimumPassesOfMatrix(matrix))


if __name__ == "__main__":
    test()
