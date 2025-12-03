def isPalindrome(string):
    L = 0
    R = len(string) - 1

    while L <= R:
        if string[L] != string[R]:
            return False

        L += 1
        R -= 1

    return True


def isPalindrome(string):  # abcdcba
    if len(string) == 0 or len(string) == 1:
        return True

    if string[0] != string[-1]:
        return False

    return isPalindrome(string[1:-1])


if __name__ == "__main__":
    print(isPalindrome("aba"))
    print(isPalindrome("a"))
    print(isPalindrome("abcdcba"))
