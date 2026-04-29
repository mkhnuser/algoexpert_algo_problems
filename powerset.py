def powerset(array):
    return recurse_powerset(array)


def recurse_powerset(array):
    res = []
    subset = []

    def dfs(i):
        if i >= len(array):
            res.append(subset.copy())
            return

        subset.append(array[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


def test():
    print(powerset([]))
    print(powerset([1, 2]))
    print(powerset([1, 2, 3]))


if __name__ == "__main__":
    test()
