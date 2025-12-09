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


def test():
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))


if __name__ == "__main__":
    test()
