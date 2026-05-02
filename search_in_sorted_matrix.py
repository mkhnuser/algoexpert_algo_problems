# def searchInSortedMatrix(matrix, target):
#     for i in range(len(matrix)):
#         array = matrix[i]
#         search_result = binary_search(
#             array=array,
#             target=target,
#             lower_index=0,
#             upper_index=len(array) - 1,
#         )
#         if search_result is not None:
#             j = search_result
#             return [i, j]
#
#     return [-1, -1]
#
#
# def binary_search(array, target, lower_index, upper_index):
#     if lower_index > upper_index:
#         return None
#
#     middle_index = (lower_index + upper_index) // 2
#     c = array[middle_index]
#
#     if c == target:
#         return middle_index
#     elif c < target:
#         return binary_search(
#             array,
#             target,
#             lower_index=middle_index + 1,
#             upper_index=upper_index,
#         )
#     return binary_search(
#         array,
#         target,
#         lower_index=lower_index,
#         upper_index=middle_index - 1,
#     )


def searchInSortedMatrix(matrix, target):
    if not matrix:
        return [-1, -1]

    i = 0
    j = len(matrix[0]) - 1

    while (i >= 0 and i <= (len(matrix) - 1)) and (
        j >= 0 and j <= (len(matrix[0]) - 1)
    ):
        element_under_consideration = matrix[i][j]

        if element_under_consideration == target:
            return [i, j]
        elif element_under_consideration > target:
            j -= 1
        else:
            i += 1

    return [-1, -1]
