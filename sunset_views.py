def sunsetViews(buildings, direction):
    # NOTE:
    # "EAST" = look from left to right.
    # "WEST" = look from right to left.
    output = []

    if direction == "EAST":
        for i in range(0, len(buildings)):
            current_height = buildings[i]
            for j in range(i + 1, len(buildings)):
                contender_height = buildings[j]
                if contender_height >= current_height:
                    break
            else:
                output.append(i)

    elif direction == "WEST":
        buildings.reverse()

        for i in range(0, len(buildings)):
            current_height = buildings[i]
            for j in range(i + 1, len(buildings)):
                contender_height = buildings[j]
                if contender_height >= current_height:
                    break
            else:
                output.append(len(buildings) - i - 1)

    else:
        raise RuntimeError("Invalid Direction has been received!")

    output.sort()
    return output


def sunsetViews(buildings, direction):
    if not buildings:
        return []

    output = []

    if direction == "EAST":
        current_maximum = buildings[-1]
        output.append(len(buildings) - 1)

        for i in reversed(
            range(len(buildings) - 1)
        ):  # NOTE: Start iteration from the second last element.
            height = buildings[i]
            if height > current_maximum:
                current_maximum = height
                output.append(i)

        output.reverse()

    elif direction == "WEST":
        current_maximum = buildings[0]
        output.append(0)

        for i in range(1, len(buildings)):
            height = buildings[i]
            if height > current_maximum:
                current_maximum = height
                output.append(i)
    else:
        raise RuntimeError("Invalid Direction!")

    return output


def sunsetViews(buildings, direction):
    stack = []

    if direction == "EAST":
        for i in range(len(buildings)):
            current_height = buildings[i]

            while stack and buildings[stack[-1]] <= current_height:
                stack.pop()

            stack.append(i)

    elif direction == "WEST":
        for i in reversed(range(len(buildings))):
            current_height = buildings[i]

            while stack and buildings[stack[-1]] <= current_height:
                stack.pop()

            stack.append(i)
        stack.reverse()
    else:
        raise RuntimeError("Invalid Direction!")

    return stack


def test():
    # ->
    buildings = [3, 5, 4, 4, 3, 1, 3, 2]
    print(sunsetViews(buildings=buildings, direction="EAST"))

    # <-
    print(sunsetViews(buildings=buildings, direction="WEST"))


if __name__ == "__main__":
    test()
