def commonCharacters(strings):
    common_chars_set = set()
    first_string = strings[0]

    for char in first_string:
        common_chars_set.add(char)

    for index in range(1, len(strings)):
        remaining_string = strings[index]
        chars = set(remaining_string)
        common_chars_set = common_chars_set.intersection(chars)

    return list(common_chars_set)


def commonCharacters(strings):
    return list(set.intersection(*(set(string) for string in strings)))


def commonCharacters(strings):
    n = len(strings)
    mapping = {}

    for string in strings:
        string_set = set(string)

        for char in string_set:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

    res = []

    for char, value in mapping.items():
        if value == n:
            res.append(char)

    return res


def commonCharacters(strings):
    potential_chars = set(strings[0])

    for index in range(1, len(strings)):
        string = strings[index]
        to_be_removed = set()
        for char in potential_chars:
            if char not in string:
                to_be_removed.add(char)
        potential_chars.difference_update(to_be_removed)

    return list(potential_chars)


if __name__ == "__main__":
    print(commonCharacters(["abc", "bcd", "cbaccd"]))
