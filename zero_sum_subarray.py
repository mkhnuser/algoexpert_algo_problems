def zeroSumSubarray(nums):
    for i in range(len(nums)):
        acc = 0

        for j in range(i, len(nums)):
            acc += nums[j]
            if acc == 0:
                return True

    return False


def zeroSumSubarray(nums):
    seen_sums = set([0])

    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)

    return False


def test():
    print(zeroSumSubarray([-5, -5, 2, 3, -2]))


if __name__ == "__main__":
    test()
