from pprint import pprint


def transposeMatrix(matrix):
    # NOTE: If n * n => n * n.
    # If n * m => m * n.
    transposed_matrix = [
        [None for __ in range(len(matrix))] for _ in range(len(matrix[0]))
    ]

    for row_index in range(len(matrix)):
        row = matrix[row_index]
        for column_index in range(len(row)):
            element_to_be_transposed = row[column_index]
            transposed_matrix[column_index][row_index] = element_to_be_transposed

    return transposed_matrix


if __name__ == "__main__":
    pprint(transposeMatrix([[1, 2]]))
    pprint(transposeMatrix([[1, 2], [3, 4], [5, 6]]))
    pprint(transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
