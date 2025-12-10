def twoNumberSum(array, targetSum):
    array.sort()
    L = 0
    R = len(array) - 1

    while L < R:
        left = array[L]
        right = array[R]
        current_sum = left + right
        if current_sum == targetSum:
            return [left, right]
        elif current_sum < targetSum:
            L += 1
        else:
            R -= 1

    return []


def twoNumberSum(array, targetSum):
    set_ = set()

    for num in array:
        diff = targetSum - num

        if diff in set_:
            return [diff, num]

        set_.add(num)

    return []


def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
