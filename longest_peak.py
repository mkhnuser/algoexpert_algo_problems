def longestPeak(array):
    if len(array) in (0, 1, 2):
        return 0

    peak_indexes = find_peak_indexes(array)

    if not peak_indexes:
        return 0

    ranges = find_peak_ranges(peak_indexes, array)
    return max(ranges.values())


def find_peak_indexes(array):
    indexes = []

    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            indexes.append(i)

    return indexes


def find_peak_ranges(peak_indexes, array):
    ranges = {}
    range_length = 0

    for i in peak_indexes:
        for j in range(i - 1, -1, -1):
            if array[j] < array[j + 1]:
                range_length += 1
            else:
                break

        for j in range(i + 1, len(array)):
            if array[j] < array[j - 1]:
                range_length += 1
            else:
                break

        ranges[i] = range_length + 1
        range_length = 0

    return ranges


def longestPeak(array):
    global_peak = 0

    for i in range(1, len(array) - 1):
        contender = array[i]
        prev = array[i - 1]
        next_ = array[i + 1]

        if contender > prev and contender > next_:
            left_length = 0
            right_length = 0

            for j in range(i - 1, -1, -1):
                if array[j] < array[j + 1]:
                    left_length += 1
                    continue
                break

            for j in range(i + 1, len(array)):
                if array[j] < array[j - 1]:
                    right_length += 1
                    continue
                break

            summation = left_length + right_length

            if summation > global_peak:
                global_peak = summation + 1

    return global_peak


def longestPeak(array):
    global_peak = 0
    i = 1

    while i <= len(array) - 2:
        contender = array[i]
        prev = array[i - 1]
        next_ = array[i + 1]
        right_bound = 0

        if contender > prev and contender > next_:
            left_length = 0
            right_length = 0

            for j in range(i - 1, -1, -1):
                if array[j] < array[j + 1]:
                    left_length += 1
                    continue
                break

            for j in range(i + 1, len(array)):
                if array[j] < array[j - 1]:
                    right_length += 1
                    right_bound += 1
                    continue
                break

            summation = left_length + right_length

            if summation > global_peak:
                global_peak = summation + 1

        i += right_bound + 1

    return global_peak


def test():
    print(longestPeak([1, 2, 3, 4]))
    print(longestPeak([5, 4, 3, 2, 1, 2, 1]))
    print(longestPeak([1, 1, 1, 2, 1, 1, 1]))
    print(longestPeak([1, 3, 2]))


if __name__ == "__main__":
    test()
