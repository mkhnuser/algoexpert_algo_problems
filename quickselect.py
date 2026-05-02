def quickselect(array, k):
    set_ = set(array)

    while k > 1:
        smallest = min(set_)
        set_.remove(smallest)
        k -= 1

    return min(set_)
