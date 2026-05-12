def threeNumberSum(array, targetSum):
    n = len(array)
    res = set()

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:
                    continue

                f = array[i]
                s = array[j]
                t = array[k]

                if f + s + t == targetSum:
                    triple = [f, s, t]
                    triple.sort()
                    res.add(tuple(triple))

    output = [list(t) for t in res]
    output.sort()
    return output


def threeNumberSum(array, targetSum):
    # NOTE: Observation: targetSum = f + s + t
    # Therefore, f = targetSum - s - t.
    # If we've seen f before, we can add [f, s, t] to our output.

    n = len(array)
    seen_numbers = set()
    output = set()

    for i in range(n):
        s = array[i]
        for j in range(i + 1, n):
            t = array[j]
            diff = targetSum - s - t
            if diff in seen_numbers:
                triplet = [diff, s, t]
                triplet.sort()
                output.add(tuple(triplet))
        seen_numbers.add(s)

    output = [list(t) for t in output]
    output.sort()
    return output


def test():
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    print(threeNumberSum(array, targetSum))


if __name__ == "__main__":
    test()
