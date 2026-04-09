# NOTE: You should find a minimum edge, but not a minimum vertex.


def find_min_min(v, edges, minimum_spanning_tree):
    min_vertex = None
    min_weight = float("+inf")

    for to, weight in edges[v]:
        if weight < min_weight and [to, weight] not in minimum_spanning_tree:
            min_vertex = to
            min_weight = weight

    return min_vertex, min_weight


def primsAlgorithm(edges):
    # NOTE: The graph is undirected.
    # NOTE: [to, weight].

    minimum_spanning_tree = []
    min_vertex = 0

    while True:
        min_vertex, min_weight = find_min_min(min_vertex, edges, minimum_spanning_tree)
        breakpoint()

        if min_vertex is None:
            break

        minimum_spanning_tree.append([min_vertex, min_weight])

    return []


def test():
    edges = [
        [[1, 3], [2, 5]],
        [[0, 3], [2, 10], [3, 12]],
        [[0, 5], [1, 10]],
        [[1, 12]],
    ]
    primsAlgorithm(edges)


if __name__ == "__main__":
    test()
