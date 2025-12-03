def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        char = string[i]

        for j in range(len(string)):
            if i == j:
                continue

            second_char = string[j]
            if second_char == char:
                break
        else:
            return i

    return -1


def firstNonRepeatingCharacter(string):
    babies = {}

    for char in string:
        if char not in babies:
            babies[char] = 1
        else:
            babies[char] += 1

    for i, char in enumerate(string):
        if babies[char] == 1:
            return i

    return -1


if __name__ == "__main__":
    print(firstNonRepeatingCharacter("abcdcaf"))
