def generateDocument(characters, document):
    if document == "":
        return True

    chars_mapping = {}
    doc_mapping = {}

    for char in characters:
        if char not in chars_mapping:
            chars_mapping[char] = 0
        chars_mapping[char] += 1

    for doc in document:
        if doc not in doc_mapping:
            doc_mapping[doc] = 0
        doc_mapping[doc] += 1

    for doc, value in doc_mapping.items():
        if doc not in chars_mapping:
            return False
        if value > chars_mapping[doc]:
            return False

    return True


def generateDocument(characters, document):
    if document == "":
        return True

    available_chars = {}

    for char in characters:
        if char not in available_chars:
            available_chars[char] = 1
        else:
            available_chars[char] += 1

    for doc_char in document:
        if doc_char not in available_chars:
            return False
        available_chars[doc_char] -= 1

    for value in available_chars.values():
        if value < 0:
            return False

    return True


if __name__ == "__main__":
    print(generateDocument(characters="abcabc", document="aabbccc"))
