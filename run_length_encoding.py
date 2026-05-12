def runLengthEncoding(string):
    if not string:
        return ""

    # NOTE: At this point, a string contains at least one character.

    turning_point = 10
    output_list = []
    i = 0
    j = 0
    n = len(string)

    while i < n and j < n:
        # NOTE: While we are within string bounds...
        current_run = (j - i) + 1
        if string[i] == string[j] and current_run < turning_point:
            j += 1
        else:
            # NOTE: The branching can be omitted,
            # but it illustrated the point nicely.
            if string[i] != string[j]:
                output_list.append(f"{current_run - 1}{string[j - 1]}")
                i = j
            else:
                # NOTE: Handle: current_run >= turning_point.
                output_list.append(f"{current_run - 1}{string[j - 1]}")
                i = j

    if i != n:
        # NOTE: There is a leftover.
        # NOTE: A..AA 10 times, for example.
        leftover_length = len(string[i:])
        leftover = string[i]
        output_list.append(f"{leftover_length}{leftover}")

    return "".join(output_list)


def test():
    string = "A"
    print(runLengthEncoding(string))
    string = "AB"
    print(runLengthEncoding(string))
    string = "AAAAAAAAAAAAABBCCCCDD"
    print(runLengthEncoding(string))


if __name__ == "__main__":
    test()
