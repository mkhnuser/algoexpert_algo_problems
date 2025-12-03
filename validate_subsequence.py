# NOTE: The first rough attempt.
def isValidSubsequence(array, sequence):
    last_j = None
    found = 0

    for i in range(len(sequence)):
        sub_el = sequence[i]

        for j in range(last_j or 0, len(array)):
            main_el = array[j]
            if main_el == sub_el:
                last_j = j + 1
                found += 1
                break

    return True if found == len(sequence) else False


# NOTE: While-loops solutions.
def isValidSubsequence(array, sequence):
    main_index = 0
    sub_index = 0

    while main_index < len(array) and sub_index < len(sequence):
        if array[main_index] == sequence[sub_index]:
            sub_index += 1

        main_index += 1

    return sub_index >= len(sequence)


# NOTE: The beautiful solution.
def isValidSubsequence(array, sequence):
    sub_index = 0

    for value in array:
        if sub_index >= len(sequence):
            break
        if value == sequence[sub_index]:
            sub_index += 1

    return sub_index >= len(sequence)


if __name__ == "__main__":
    print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
