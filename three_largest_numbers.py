def findThreeLargestNumbers(array):
    res = [None, None, None]

    for num in array:
        for i in reversed(range(len(res))):
            res_el = res[i]
            if res_el is None or num > res_el:
                if i == 1:
                    res[i - 1] = res_el
                if i == 2:
                    res[i - 2] = res[i - 1]
                    res[i - 1] = res_el
                res[i] = num
                break

    return res


def test():
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))


if __name__ == "__main__":
    test()
