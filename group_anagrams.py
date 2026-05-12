def groupAnagrams(words):
    mapping = {}
    for word in words:
        # key = compute_key_dict(word)  # NOTE: Just use "".join(sorted(word))!!!
        key = "".join(sorted(word))

        if key not in mapping:
            mapping[key] = set()

        mapping[key].add(word)

    return [list(value) for value in mapping.values()]


def compute_key_dict(word):
    counter = {}

    for char in word:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1

    sorted_items = sorted(counter.items())
    key = repr(sorted_items)
    return key


def test():
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(groupAnagrams(words))


if __name__ == "__main__":
    test()
