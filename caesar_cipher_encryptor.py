a_ord = ord("a")


def caesarCipherEncryptor(string, key):
    if key == 0:
        return string

    result_list = []

    for char in string:
        shifted_ord = ord(char) - a_ord
        destination_ord = shifted_ord + key
        destination_ord %= 26
        destination_ord += a_ord
        result_list.append(chr(destination_ord))

    return "".join(result_list)


if __name__ == "__main__":
    print(caesarCipherEncryptor("abc", 1))
    print(caesarCipherEncryptor("abc", 26))
