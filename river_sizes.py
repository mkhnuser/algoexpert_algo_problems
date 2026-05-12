# NOTE: A BFS solution.
# from collections import deque
#
#
# DIRECTIONS = (
#     (0, +1),  # top
#     (+1, 0),  # right
#     (0, -1),  # buttom
#     (-1, 0),  # left
# )
# RIVER_ITEM = 1
#
#
# def bfs(coords, matrix, visited):
#     counter = 0
#     i, j = coords
#     d = deque()
#     d.append((i, j))
#
#     while d:
#         c = d.popleft()
#         i, j = c
#
#         if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]):
#             continue
#
#         if matrix[i][j] != RIVER_ITEM or (i, j) in visited:
#             continue
#
#         visited.add((i, j))
#         counter += 1
#
#         for direction in DIRECTIONS:
#             i_increment, j_increment = direction
#             next_i = i + i_increment
#             next_j = j + j_increment
#             d.append((next_i, next_j))
#
#     return counter
#
#
# def riverSizes(matrix):
#     # NOTE: Given a matrix,
#     # 1. Iterate over it.
#     # 2. If 1 is encountered and the node has not been visited, explore the river part using bfs.
#     # 3. Mark the whole river part as visited.
#     # 4. Continue.
#
#     # NOTE: A set of visited 1s coords.
#     visited = set()
#     output_list = []
#
#     for i in range(len(matrix)):
#         row = matrix[i]
#         for j in range(len(row)):
#             value = row[j]
#             if value == RIVER_ITEM and (i, j) not in visited:
#                 output_list.append(bfs((i, j), matrix, visited))
#
#     return output_list
#
#
# def test():
#     matrix = [
#         [1, 0, 0, 1, 0],
#         [1, 0, 1, 0, 0],
#         [0, 0, 1, 0, 1],
#         [1, 0, 1, 0, 1],
#         [1, 0, 1, 1, 0],
#     ]
#     print(riverSizes(matrix))
#
#
# if __name__ == "__main__":
#     test()


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)
RIVER_ITEM = 1


def dfs(i, j, n, m, matrix, visited_set):
    if (
        i < 0
        or i >= n
        or j < 0
        or j >= m
        or ((i, j) in visited_set)
        or matrix[i][j] != 1
    ):
        return 0

    # NOTE: matrix[i][j] == 1 at this point.
    visited_set.add((i, j))
    counter = 0

    for direction in DIRECTIONS:
        i_incr, j_incr = direction
        counter += dfs(i + i_incr, j + j_incr, n, m, matrix, visited_set)

    return 1 + counter


# NOTE: A DFS solution.
def riverSizes(matrix):
    output_list = []

    n = len(matrix)
    m = len(matrix[0])
    visited_set = set()

    for i in range(n):
        for j in range(m):
            dfs_result = dfs(i, j, n, m, matrix, visited_set)
            if dfs_result != 0:
                output_list.append(dfs_result)

    return output_list


def test():
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    print(riverSizes(matrix))


if __name__ == "__main__":
    test()
