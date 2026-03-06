def getPermutations(array):
    if not array:
        return array

    perms = []
    helper(array, [], perms)
    return perms


def helper(array, perm, perms):
    if not array:
        perms.append(perm)
    else:
        for i in range(len(array)):
            new_array = array.copy()
            new_array.pop(i)

            leading_number = array[i]

            new_perm = perm.copy()
            new_perm.append(leading_number)

            helper(new_array, new_perm, perms)


def test():
    print(getPermutations([]))
    print(getPermutations([1, 2]))
    print(getPermutations([1, 2, 3]))


if __name__ == "__main__":
    test()
