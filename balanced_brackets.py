def balancedBrackets(string):
    stack = []

    for char in string:
        if char not in "([{}])":
            continue

        if char in ("(", "[", "{"):
            stack.append(char)
        else:
            if not stack:
                return False

            opening_char = stack.pop()

            if (
                (char == ")" and opening_char != "(")
                or (char == "]" and opening_char != "[")
                or (char == "}" and opening_char != "{")
            ):
                return False

    return len(stack) == 0


def test():
    assert balancedBrackets("()")
    assert not balancedBrackets("(")
    assert not balancedBrackets(")")
    assert balancedBrackets("()[]{}")
    assert not balancedBrackets("())")
    assert balancedBrackets("(([{}]))[]{}")
    assert balancedBrackets("")
    assert balancedBrackets("(a)")


if __name__ == "__main__":
    test()
