def nextGreaterElement(array):
    if not array:
        return array

    maximum_index = 0

    for i in range(1, len(array)):
        if array[i] > array[maximum_index]:
            maximum_index = i

    maximum_indexes = []
    maximum_number = array[maximum_index]

    for i, num in enumerate(array):
        if num == maximum_number:
            maximum_indexes.append(i)

    stack = []
    stack.append(array[maximum_index])

    for i in range(maximum_index - 1, maximum_index - len(array), -1):
        current_element = array[i]

        while stack and stack[-1] <= current_element:
            stack.pop()
        if stack and stack[-1] > current_element:
            array[i] = stack[-1]

        stack.append(current_element)

    for i in maximum_indexes:
        array[i] = -1

    return array


def nextGreaterElement(array):
    if not array:
        return array

    n = len(array)

    output = [-1] * n

    for i in range(n):
        for j in range(i - 1, i - n, -1):
            contender = array[j]
            current = array[i]

            if contender > current:
                output[i] = array[j]

    return output


def test():
    print(nextGreaterElement([2, 5, -3, -4, 6, 7, 2]))
    #
    print(nextGreaterElement([1, 0, 1, 0, 1, 0, 1]))
    # NOTE: EXPECTED:
    # [5, 6, 6, 6, 7, -1, 5]
    # [-1, 1, -1, 1, -1, 1, -1].


if __name__ == "__main__":
    test()
