def getNthFib(n):
    # NOTE: The problem states that:
    # f(1) == 0 and f(2) == 1.
    if n == 1:
        return 0
    if n == 2:
        return 1

    return getNthFib(n - 2) + getNthFib(n - 1)


# NOTE: OK, what about an iterative approach?


def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    assert n > 2
    pass
