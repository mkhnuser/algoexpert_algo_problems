def runLengthEncoding(string):
    i = 0
    j = 0
    n = len(string)

    if n == 0:
        return string

    result = []

    while i < n:
        if string[i] == string[j]:
            i += 1
        else:
            result.append(f"{(i - j)}{string[j]}")
            j = i

        if (i - j) + 1 >= 9:
            if i >= n:
                i -= 1
            if string[i] == string[j]:
                result.append(f"{i - j + 1}{string[j]}")
                i += 1
                j = i

    if j < i:
        result.append(f"{len(string[j:i])}{string[j]}")

    return "".join(result)


def runLengthEncoding(string):
    chars = []
    run_length = 1

    # NOTE: AAABB
    for i in range(1, len(string)):
        current_char = string[i]
        prev_char = string[i - 1]

        if current_char != prev_char or run_length >= 9:
            chars.append(str(run_length))
            chars.append(prev_char)
            run_length = 0

        run_length += 1

    chars.append(str(run_length))
    chars.append(string[len(string) - 1])
    return "".join(chars)


if __name__ == "__main__":
    print(runLengthEncoding("                          "))
