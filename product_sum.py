def productSum(array):
    return recurse(array, depth=1)


def recurse(array, depth):
    summation = 0

    for el in array:
        if isinstance(el, int):
            summation += el
        else:
            summation += (depth + 1) * recurse(el, depth + 1)

    return summation


def recurse(array, depth):
    return depth * sum(
        el if isinstance(el, int) else recurse(el, depth + 1) for el in array
    )


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
