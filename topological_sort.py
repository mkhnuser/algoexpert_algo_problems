def _has_cycle(job, adj_list, colors):
    colors[job] = "gray"

    for n in adj_list[job]:
        if colors[n] == "gray":
            return True

        if colors[n] == "white":
            if _has_cycle(n, adj_list, colors):
                return True

    colors[job] = "black"
    return False


def has_cycle(jobs, adj_list):
    # NOTE: jobs are just distinct ints.
    colors = {job: "white" for job in jobs}

    for job in jobs:
        if colors[job] == "white":
            if _has_cycle(job, adj_list, colors):
                return True

    return False


def _dfs(job, adj_list, colors, entry, leave, time):
    time += 1
    colors[job] = "gray"
    entry[job] = time

    for n in adj_list[job]:
        if colors[n] == "white":
            time = _dfs(n, adj_list, colors, entry, leave, time)

    time += 1
    leave[job] = time
    colors[job] = "black"
    return time


def dfs(jobs, adj_list):
    # NOTE: jobs are just distinct ints.
    colors = {job: "white" for job in jobs}
    entry = {job: 0 for job in jobs}
    leave = {job: 0 for job in jobs}
    time = 0

    for job in jobs:
        if colors[job] == "white":
            time = _dfs(job, adj_list, colors, entry, leave, time)

    return list(
        item[0]
        for item in sorted(leave.items(), key=lambda item: item[-1], reverse=True)
    )


def topologicalSort(jobs, deps):
    # NOTE:
    # Topological Sort is only possible on DAGs.
    # So:
    # 1. Ensure the input graph has no cycles.
    # 2. Use DFS to compute leave times.
    # 3. Use leave times to determine a topological ordering.

    adj_list = {}

    for dep in deps:
        first, second = dep
        if first not in adj_list:
            adj_list[first] = []
        adj_list[first].append(second)

    for job in jobs:
        if job not in adj_list:
            adj_list[job] = []

    if has_cycle(jobs, adj_list):
        return []

    # NOTE: There is no cycle at this point.
    return dfs(jobs, adj_list)


def test():
    jobs = [1, 2]
    deps = [[1, 2], [2, 1]]
    print(topologicalSort(jobs, deps))

    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    print(topologicalSort(jobs, deps))


if __name__ == "__main__":
    test()
