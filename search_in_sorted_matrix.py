def searchInSortedMatrix(matrix, target):
    # NOTE: O(n * log(n)).
    for row_index in range(len(matrix)):
        search_result = bin_search_row(matrix[row_index], target)
        if search_result is not None:
            return [row_index, search_result]

    return [-1, -1]


def bin_search_row(row, target):
    left = 0
    right = len(row) - 1

    while left <= right:
        middle = (left + right) // 2
        el = row[middle]
        if el == target:
            return middle
        elif el > target:
            right = middle - 1
        else:
            left = middle + 1

    return None


def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        val = matrix[row][col]

        if target == val:
            return [row, col]

        if val < target:
            row += 1
        elif val > target:
            col -= 1

    return [-1, -1]


def test():
    print(
        searchInSortedMatrix(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
            ],
            target=9,
        )
    )


if __name__ == "__main__":
    test()
