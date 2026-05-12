def generateDocument(characters, document):
    if document == "":
        return True

    characters_frequency_mapping = {}

    for char in characters:
        if char not in characters_frequency_mapping:
            characters_frequency_mapping[char] = 0
        characters_frequency_mapping[char] += 1

    document_frequency_mapping = {}

    for char in document:
        if char not in document_frequency_mapping:
            document_frequency_mapping[char] = 0
        document_frequency_mapping[char] += 1

    for char in document:
        if char not in characters_frequency_mapping:
            return False

        if characters_frequency_mapping[char] < document_frequency_mapping[char]:
            return False

    return True


def generateDocument(characters, document):
    if document == "":
        return True

    frequency_mapping = {}

    for char in document:
        if char not in frequency_mapping:
            frequency_mapping[char] = 0
        frequency_mapping[char] -= 1

    for char in characters:
        if char not in frequency_mapping:
            frequency_mapping[char] = 0
        frequency_mapping[char] += 1

    for char, freq in frequency_mapping.items():
        if freq < 0:
            return False

    return True
