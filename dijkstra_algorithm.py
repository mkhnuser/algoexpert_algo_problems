import math


def find_min_distance_vertex(edges, distances, visited):
    min_distance_vertex = None
    min_distance = float("+inf")

    for v, distance in enumerate(distances):
        if distance < min_distance and visited[v] is None:
            min_distance_vertex = v
            min_distance = distance

    return min_distance_vertex


def relax(u, v, w, distances):
    if distances[v] > distances[u] + w:
        distances[v] = distances[u] + w


def dijkstrasAlgorithm(start, edges):
    n = len(edges)
    distances = [float("+inf") for _ in range(n)]
    visited = [None for _ in range(n)]

    distances[start] = 0

    while True:
        min_distance_vertex = find_min_distance_vertex(edges, distances, visited)

        if min_distance_vertex is None:
            break

        for neighbor, w in edges[min_distance_vertex]:
            relax(min_distance_vertex, neighbor, w, distances)

        visited[min_distance_vertex] = True

    return list(map(lambda x: -1 if math.isinf(x) else x, distances))


def test():
    edges = [
        [[1, 7]],
        [[2, 6], [3, 20], [4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        [],
    ]
    dijkstrasAlgorithm(0, edges)


if __name__ == "__main__":
    # test()
    pass
