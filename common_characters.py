def commonCharacters(strings):
    common_characters = set(strings[0])

    for string in strings[1:]:
        string_set = set(string)
        common_characters.intersection_update(string_set)

    return list(common_characters)


def test():
    input_ = ["abc", "bcd", "cbaccd"]
    print(commonCharacters(input_))


if __name__ == "__main__":
    test()
