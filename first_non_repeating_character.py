def firstNonRepeatingCharacter(string):
    mapping = {}
    # NOTE: Store character -> [count, index].

    for i, char in enumerate(string):
        if char not in mapping:
            mapping[char] = [0, i]
        mapping[char][0] += 1

    for char in mapping:
        count, index = mapping[char]
        if count == 1:
            return index

    return -1


a_ord = ord("a")


def firstNonRepeatingCharacter(string):
    n = len(string)
    counter = [0] * 26

    for i, char in enumerate(string):
        char_ord = ord(char) - a_ord
        counter[char_ord] += 1

    for i in range(n):
        char = string[i]
        char_ord = ord(char)
        shifted_ord = char_ord - a_ord
        if counter[shifted_ord] == 1:
            return i

    return -1
