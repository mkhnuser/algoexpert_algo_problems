def majorityElement(array):
    # NOTE: majority element occupies over half of array's indexes.
    majority_element = array[0]
    majority_element_score = 0

    for i in range(len(array)):
        element_score = 0

        for j in range(len(array)):
            if array[i] == array[j]:
                element_score += 1

        if element_score > majority_element_score:
            majority_element_score = element_score
            majority_element = array[i]

    assert majority_element_score > len(array) // 2, (
        "Your assumption is outright incorrect."
    )
    return majority_element


def majorityElement(array):
    majority_element = array[0]
    count = 1

    for i in range(1, len(array) - 1):
        if array[i] == majority_element:
            count += 1
        else:
            count -= 1

        if count <= 0:
            majority_element = array[i + 1]
            count = 0

    return majority_element


def test():
    array = [1, 2, 3, 2, 2, 1, 2]
    # NOTE:  0  1  2  3  4  5  6
    # len(array) = 7
    # The element 2 occupies 4 / 7 indexes.
    print(majorityElement(array))


if __name__ == "__main__":
    test()
