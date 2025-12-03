def twoNumberSum(array, targetSum):
    array.sort()
    L = 0
    R = len(array) - 1

    while L <= R:
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


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
