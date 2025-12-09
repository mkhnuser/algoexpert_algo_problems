def bestDigits(number, numDigits):
    max_num_of_removals = numDigits
    stack = []

    for i in range(len(number)):
        char = number[i]
        integer = int(char)

        if not stack:
            stack.append(integer)
            continue

        while max_num_of_removals > 0 and stack and stack[-1] <= integer:
            stack.pop()
            max_num_of_removals -= 1

        stack.append(integer)

    while max_num_of_removals > 0:
        stack.pop()
        max_num_of_removals -= 1

    return "".join(map(str, stack))


def test():
    print(bestDigits("462839", 2))
    print(bestDigits("129847563", 4))  # 98763
    print(bestDigits("321", 1))
    print(bestDigits("321", 2))


if __name__ == "__main__":
    test()
