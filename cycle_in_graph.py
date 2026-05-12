def _dfs(v, edges, colors):
    colors[v] = "gray"

    for n in edges[v]:
        if colors[n] == "gray":
            return True

        if colors[n] == "white":
            has_cycle = _dfs(n, edges, colors)
            if has_cycle:
                return has_cycle

    colors[v] = "black"
    return False


def dfs(edges):
    colors = ["white"] * len(edges)

    for v in range(len(edges)):
        if colors[v] == "white":
            if _dfs(v, edges, colors):
                return True

    return False


def cycleInGraph(edges):
    return dfs(edges)


def test():
    edges = [
        [1, 3],  # 0
        [2, 3, 4],  # 1
        [0],  # 2
        [],  # 3
        [2, 5],  # 4
        [],  # 5
    ]
    print(cycleInGraph(edges))


if __name__ == "__main__":
    test()
