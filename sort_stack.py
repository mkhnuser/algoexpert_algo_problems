def sortStack(stack):
    # NOTE: ALLOWED OPERATIONS: append; pop; [-1].
    if len(stack) == 0 or len(stack) == 1:
        return stack

    # [3, 2, 1]
    # [2, 3] 1
    # [2, 1, 3]
    popped = stack.pop()

    sortStack(stack)

    if popped > stack[-1]:
        stack.append(popped)
    else:
        # NOTE: popped <= the last element on a stack.
        greater = stack.pop()
        stack.append(popped)
        sortStack(stack)
        stack.append(greater)

    return stack


def test():
    print(sortStack([]))
    print(sortStack([1]))
    print(sortStack([2, 1]))
    print(sortStack([1, 2]))
    print(sortStack([2, 1, 3]))
    print(sortStack([3, 2, 1]))
    print(sortStack([1, 2, 3]))
    print(sortStack([2, 3, 1]))


if __name__ == "__main__":
    test()
