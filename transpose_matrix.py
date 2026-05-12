from pprint import pprint


def transposeMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    output = [[None for __ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            output[j][i] = matrix[i][j]

    return output


if __name__ == "__main__":
    pprint(transposeMatrix([[1, 2]]))
    pprint(transposeMatrix([[1, 2], [3, 4], [5, 6]]))
    pprint(transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
