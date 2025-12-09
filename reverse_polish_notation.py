def reversePolishNotation(tokens):
    stack = []

    for token in tokens:
        if str.isnumeric(token.lstrip("+-")):
            stack.append(int(token))
        else:
            number_two = stack.pop()
            number_one = stack.pop()

            if token == "+":
                res = number_one + number_two
                stack.append(res)
            elif token == "-":
                res = number_one - number_two
                stack.append(res)
            elif token == "/":
                res = int(number_one / number_two)
                stack.append(res)
            elif token == "*":
                res = number_one * number_two
                stack.append(res)
            else:
                raise RuntimeError("Invalid Operator has been received!")

    return stack[-1]


def test():
    print(reversePolishNotation(["50", "3", "17", "+", "2", "-", "/"]))
    print(reversePolishNotation(["-5", "2", "+"]))


if __name__ == "__main__":
    test()
