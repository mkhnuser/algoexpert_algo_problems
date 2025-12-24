import itertools as it
import functools as ft
import operator as op


def arrayOfProducts(array):
    # NOTE: [5, 1, 4, 2].
    output = []

    for i in range(len(array)):
        acc = 1

        for j in range(len(array)):
            if i == j:
                continue
            acc *= array[j]

        output.append(acc)

    return output


def arrayOfProducts(array):
    # NOTE: [5, 1, 4, 2].
    output = []

    for i in range(len(array)):
        prev = array[i]
        array[i] = 1
        output.append(
            ft.reduce(
                op.mul,
                array,
                1,
            )
        )
        array[i] = prev

    return output


def arrayOfProducts(array):
    # NOTE: [5, 1, 4, 2].
    output = []

    for i in range(len(array)):
        left_acc = 1
        for j in range(0, i):
            left_acc *= array[j]

        right_acc = 1
        for j in range(i + 1, len(array)):
            right_acc *= array[j]

        output.append(left_acc * right_acc)

    return output


def arrayOfProducts(array):
    # NOTE: [5, 1, 4, 2].
    output = []
    left = [1] * len(array)  # NOTE: It will be [1, 5, 20, 40]
    right = [1] * len(array)  # NOTE: It will be [8, 8, 2, 1]

    product = 1
    for i in range(1, len(array) + 1):
        left[i - 1] = product
        product *= array[i - 1]

    product = 1
    for i in range(len(array) - 1 - 1, -1 - 1, -1):
        right[i + 1] = product
        product *= array[i + 1]

    for i in range(len(array)):
        output.append(left[i] * right[i])

    return output


def test():
    print(arrayOfProducts([5, 1, 4, 2]))


if __name__ == "__main__":
    test()
