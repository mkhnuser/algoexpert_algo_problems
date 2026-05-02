# def staircaseTraversal(height, maxSteps):
#     if height == 1 or height == 0:
#         return 1
#
#     num_of_ways = 0
#
#     for k in range(1, maxSteps + 1):
#         height_to_examine = height - k
#         if height_to_examine >= 0:
#             num_of_ways += staircaseTraversal(height_to_examine, maxSteps)
#
#     return num_of_ways


def staircaseTraversal(height, maxSteps):
    dp = [0] * (height + 1)
    dp[0] = 1
    dp[1] = 1

    for current_height in range(2, height + 1):
        # NOTE: Use max() to avoid "overflow": for example, consider a case when height = 4 and maxSteps = 3.
        start_height = max(current_height - maxSteps, 0)
        dp[current_height] = sum(dp[start_height:current_height])

    return dp[-1]


def test():
    print(staircaseTraversal(3, 2))
    print(staircaseTraversal(4, 2))
    print(staircaseTraversal(4, 3))


if __name__ == "__main__":
    test()
