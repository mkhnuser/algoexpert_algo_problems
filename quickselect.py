def quickselect(array, k):
    # NOTE: kth smallest.
    nums = set(array)

    while k > 1:
        smallest = min(nums)
        nums.remove(smallest)
        k -= 1

    return min(nums)


def test():
    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3
    assert quickselect(array, k) == 5


if __name__ == "__main__":
    test()
