def prepare_output(mst_list, n):
    output = [None] * n

    for tuple_ in mst_list:
        v1, (v2, weight) = tuple_
        if output[v1] is None:
            output[v1] = []
        if output[v2] is None:
            output[v2] = []
        output[v1].append([v2, weight])
        output[v2].append([v1, weight])

    return output


def transform_edges(edges):
    # NOTE: Just make the edges tuples, but not lists, so that the edges are hashable.
    new_edges = []

    for list_ in edges:
        new_adj_list = []
        for edge in list_:
            e = tuple(edge)
            new_adj_list.append(e)
        new_edges.append(tuple(new_adj_list))

    return new_edges


def find_edge_with_min_weight_and_not_in_mst_yet_and_is_incident_on_mst(
    edges,
    added_vertices,
):
    min_edge = None
    min_weight = float("+inf")

    for v, incident_edges in enumerate(edges):
        if v not in added_vertices:
            # NOTE: We are growing our MST out of the existing MST.
            continue

        for incident_edge in incident_edges:
            destination_vertex, weight = incident_edge
            if (weight < min_weight) and (destination_vertex not in added_vertices):
                min_edge = v, incident_edge
                min_weight = weight

    return min_edge


def primsAlgorithm(edges):
    edges = transform_edges(edges)
    n = len(edges)
    not_added_vertices = set(range(0, n))
    added_vertices = set()
    mst = set()

    # NOTE: We are guaranteed to have at least one vertex.
    # Since the enumeration starts from 0, this vertex is bound to be zero.
    added_vertices.add(0)
    not_added_vertices.remove(0)

    # NOTE: We are guaranteed that the graph is connected.
    while not_added_vertices:
        min_edge = find_edge_with_min_weight_and_not_in_mst_yet_and_is_incident_on_mst(
            edges,
            added_vertices,
        )

        if min_edge is None:
            break

        v, edge = min_edge
        mst.add((v, edge))
        added_vertices.add(v)
        added_vertices.add(edge[0])
        not_added_vertices.discard(v)
        not_added_vertices.discard(edge[0])

    mst_list = list(mst)
    return prepare_output(mst_list, n)


def test():
    edges = [
        [[1, 3], [2, 5]],  # 0
        [[0, 3], [2, 10], [3, 12]],  # 1
        [[0, 5], [1, 10]],  # 2
        [[1, 12]],  # 3
    ]
    print(primsAlgorithm(edges))

    edges = [
        [[1, 7], [2, 5]],
        [[0, 7], [2, 6], [3, 20], [4, 3]],
        [[0, 5], [1, 6], [3, 14]],
        [[1, 20], [2, 14], [4, 2]],
        [[1, 3], [3, 2]],
    ]
    print(primsAlgorithm(edges))


if __name__ == "__main__":
    test()
