def getNthFib(n):
    # NOTE: The problem states that:
    # f(1) == 0 and f(2) == 1.
    if n == 1:
        return 0
    if n == 2:
        return 1

    return getNthFib(n - 2) + getNthFib(n - 1)


def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    assert n >= 3
    n -= 2

    a = 0
    b = 1

    while n > 0:
        c = a + b
        a, b = b, c
        n -= 1

    return c


def getNthFib(n):
    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, a + b

    return a


def getNthFib(n):
    memo = {}

    def get_nth_fib(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n in memo:
            return memo[n]
        else:
            memo[n] = get_nth_fib(n - 1) + get_nth_fib(n - 2)

        return memo[n]

    return get_nth_fib(n)


def test():
    assert getNthFib(1) == 0
    assert getNthFib(2) == 1
    assert getNthFib(3) == 1
    assert getNthFib(4) == 2
    assert getNthFib(5) == 3
    assert getNthFib(6) == 5
    assert getNthFib(7) == 8


if __name__ == "__main__":
    test()
