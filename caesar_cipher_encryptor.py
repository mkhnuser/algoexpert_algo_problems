import string as s


def caesarCipherEncryptor(string, key):
    mapping = {}

    for i in range(len(s.ascii_lowercase)):
        char = s.ascii_lowercase[i]
        associated_char = s.ascii_lowercase[(i + key) % len(s.ascii_lowercase)]
        mapping[char] = associated_char

    translation_table = str.maketrans(mapping)
    return string.translate(translation_table)


if __name__ == "__main__":
    print(caesarCipherEncryptor("abc", 2))
