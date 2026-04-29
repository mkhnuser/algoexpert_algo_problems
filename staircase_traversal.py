def staircaseTraversal(height, maxSteps):
    if height == 1 or height == 0:
        return 1

    num_of_ways = 0

    for k in range(1, maxSteps + 1):
        height_to_examine = height - k
        if height_to_examine >= 0:
            num_of_ways += staircaseTraversal(height_to_examine, maxSteps)

    return num_of_ways


def test():
    print(staircaseTraversal(3, 2))
    print(staircaseTraversal(4, 2))


if __name__ == "__main__":
    test()
