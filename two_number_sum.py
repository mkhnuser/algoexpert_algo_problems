def twoNumberSum(array, targetSum):
    output = []

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return output


def twoNumberSum(array, targetSum):
    output = []
    seen = set()
    for num in array:
        diff = targetSum - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
    return output


def twoNumberSum(array, targetSum):
    array.sort()
    if not array:
        return []

    l = 0
    r = len(array) - 1
    while l < r:
        L = array[l]
        R = array[r]
        current_summation = L + R
        if current_summation == targetSum:
            return [L, R]
        elif current_summation > targetSum:
            r -= 1
        else:
            l += 1

    return []
