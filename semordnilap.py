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


def is_palind(w1, w2):
    return w1[::-1] == w2


def semordnilap(words):
    mapping = {}
    for word in words:
        mapping[word] = set()
        mapping[word].add(word)

    for word in words:
        for m_word in mapping:
            if is_palind(word, m_word):
                mapping[m_word].add(word)

    output_set = set()
    for group in mapping.values():
        group = list(group)
        if len(group) <= 1:
            continue
        group.sort()
        output_set.add(tuple(group))

    return [list(group) for group in output_set]


def semordnilap(words):
    seen_words = set()
    output = []

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in seen_words:
            output.append([word, reversed_word])
        seen_words.add(word)

    return output


if __name__ == "__main__":
    print(semordnilap(["diaper", "repaid"]))
    print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))
