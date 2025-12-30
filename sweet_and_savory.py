def sweetAndSavory(dishes, target):
    # NOTE: your pairing should never be more savory than the target.
    if all(dish > 0 for dish in dishes) or all(dish < 0 for dish in dishes):
        return [0, 0]

    output = [0, 0]
    closest = float("+inf")

    for dish in dishes:
        if dish < 0:
            # NOTE: The dish is sweet.
            for another_dish in dishes:
                if another_dish < 0:
                    continue

                # NOTE: At this point another_dish is savory.
                score = dish + another_dish

                if score > target:
                    continue

                if abs(target - score) < closest:
                    closest = abs(target - score)
                    output[0] = dish
                    output[1] = another_dish
        elif dish > 0:
            # NOTE: The dish is savory.
            for another_dish in dishes:
                if another_dish > 0:
                    continue

                # NOTE: At this point another_dish is sweet.
                score = dish + another_dish

                if score > target:
                    continue

                if abs(target - score) < closest:
                    closest = abs(target - score)
                    output[0] = another_dish
                    output[1] = dish
        else:
            raise RuntimeError("Zero is not permitted.")

    return output


def test():
    dishes = [-3, -5, 1, 7]
    target = 8
    print(sweetAndSavory(dishes, target))

    dishes = [1, 2, 10, 8]
    target = 8
    print(sweetAndSavory(dishes, target))

    dishes = [-1, -2, -6, -4]
    target = 8
    print(sweetAndSavory(dishes, target))


if __name__ == "__main__":
    test()
