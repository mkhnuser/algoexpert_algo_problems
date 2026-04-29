from pprint import pprint


digit_to_letters_mapping = {
    0: [],
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


def generate_mnemonics_recursively(numbers, current_mnemonic, output):
    # NOTE: 1 9 0 5.
    # NOTE: Order of numbers matters, so you should preserve it somehow.
    # NOTE: A mnemonic only contains letters or zero or one.

    if not numbers:
        output.append(current_mnemonic)
        return

    num = numbers[0]
    if num == 0:
        generate_mnemonics_recursively(
            numbers=numbers[1:],
            current_mnemonic=current_mnemonic + "0",
            output=output,
        )
    elif num == 1:
        generate_mnemonics_recursively(
            numbers=numbers[1:],
            current_mnemonic=current_mnemonic + "1",
            output=output,
        )
    else:
        for char in digit_to_letters_mapping[num]:
            generate_mnemonics_recursively(
                numbers=numbers[1:],
                current_mnemonic=current_mnemonic + char,
                output=output,
            )


def generate_mnemonics_iteratively(numbers):
    # NOTE: 1 9 0 5.
    # NOTE: Order of numbers matters, so you should preserve it somehow.
    # NOTE: A mnemonic only contains letters or zero or one.
    output = [""]

    for num in numbers:
        t = []

        if num == 0:
            for o in output:
                o += "0"
                t.append(o)
            output = t
        elif num == 1:
            for o in output:
                o += "1"
                t.append(o)
            output = t
        else:
            for char in digit_to_letters_mapping[num]:
                for o in output:
                    o += char
                    t.append(o)
            output = t

    return output


def phoneNumberMnemonics(phoneNumber):
    phone_number = phoneNumber
    assert len(phone_number) >= 1

    numbers = [int(char) for char in phoneNumber]
    # output = []
    # generate_mnemonics_recursively(numbers=numbers, current_mnemonic="", output=output)
    output = generate_mnemonics_iteratively(numbers=numbers)
    return output


def test():
    pprint(phoneNumberMnemonics("1905"))


if __name__ == "__main__":
    test()
