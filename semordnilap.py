def semordnilap(words):
    mapping = {}

    # NOTE: diaper <-> repaid.
    for word in words:
        freeze = frozenset(word)

        if freeze not in mapping:
            mapping[freeze] = set([word])
        else:
            mapping[freeze].add(word)

    # NOTE: We want to return only pairs.
    return list(list(value) for value in mapping.values() if len(list(value)) > 1)


if __name__ == "__main__":
    print(semordnilap(["diaper", "repaid"]))
    print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))
