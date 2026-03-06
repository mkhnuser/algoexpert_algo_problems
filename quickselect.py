def quickselect(array, k):
    # NOTE: kth smallest.
    nums = set(array)

    while k > 1:
        smallest = min(nums)
        nums.remove(smallest)
        k -= 1

    return min(nums)


def quickselect(array, k):
    return recurse_quick_select(array, k, 0, len(array) - 1)


def recurse_quick_select(array, k, l, r):
    pivot = array[l]
    left_index = l + 1
    right_index = r

    while left_index <= right_index:
        left_element = array[left_index]
        right_element = array[right_index]

        if left_element > pivot and right_element < pivot:
            array[left_index], array[right_index] = (
                array[right_index],
                array[left_index],
            )
            left_index += 1
            right_index -= 1

        elif left_element <= pivot:
            left_index += 1
        elif right_element >= pivot:
            right_index -= 1

    array[l], array[right_index] = array[right_index], array[l]

    position = k - 1
    if position == right_index:
        return array[right_index]
    elif position > right_index:
        return recurse_quick_select(array, k, right_index + 1, r)
    else:
        return recurse_quick_select(array, k, l, right_index - 1)


def test():
    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3
    assert quickselect(array, k) == 5


if __name__ == "__main__":
    test()
