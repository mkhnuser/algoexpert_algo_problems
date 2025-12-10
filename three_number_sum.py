def threeNumberSum(array, targetSum):
    output = []

    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            for k in range(len(array)):
                if i == k or j == k:
                    continue
                # NOTE: i != k and j != k and i != j.

                one = array[i]
                two = array[j]
                three = array[k]

                if one + two + three == targetSum:
                    to_be_added = {one, two, three}
                    if to_be_added not in output:
                        output.append(to_be_added)

    res = [list(sorted(list(o))) for o in output]
    return list(sorted(res))


def threeNumberSum(array, targetSum):
    array.sort()
    i = 0
    j = len(array) - 1

    # NOTE: a + b + c == target.

    output = []
    added = set()
    i = 0
    j = len(array) - 1

    # NOTE: This loop takes O(n ** 2)
    for k in range(len(array)):
        while i < j:
            if k == i:
                # NOTE: We don't want to consider the same number.
                i += 1
                continue
            elif k == j:
                # NOTE: We don't want to consider the same number.
                j -= 1
                continue

            a = array[k]
            b = array[i]
            c = array[j]
            summation = a + b + c

            if summation == targetSum:
                frozen = frozenset((a, b, c))
                if frozen not in added:
                    output.append([a, b, c])
                added.add(frozen)
                i += 1
                j -= 1
            elif summation < targetSum:
                i += 1
            else:
                j -= 1

        i = 0
        j = len(array) - 1

    # NOTE: Sort output as required by the problem statement.
    output = [list(sorted(el)) for el in output]
    return list(sorted(output))


def test():
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
    print(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))


if __name__ == "__main__":
    test()
