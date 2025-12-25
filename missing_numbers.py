def missingNumbers(nums):
    # NOTE: range of nums is [1, n], where n = len(nums) + 2.
    # nums are unordered and unique.
    # input: [1, 4, 3].
    # output: [2, 5].
    nums_set = set(nums)  # NOTE: {1, 4, 3}.
    output = []  # NOTE: [].

    for num in range(1, (len(nums) + 2) + 1):
        if num not in nums_set:
            output.append(num)

    return output
