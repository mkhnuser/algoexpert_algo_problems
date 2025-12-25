def bestSeat(seats):
    # NOTE: zeroes represent empty seats.
    # The input array has a length of at least one.
    # 1s are placed at the either end of the array: [1, ..., 1].
    candidate_indexes = []

    for i in range(len(seats)):
        if seats[i] == 0:
            candidate_indexes.append(i)

    return find_the_best_seat(candidate_indexes) if candidate_indexes else -1


def find_the_best_seat(candidate_indexes):
    # NOTE: At this point we have at least one candidate seat.

    # NOTE: [1, 3, 4, 5]
    #        0  1  2  3

    the_best_seat = candidate_indexes[0]
    the_best_range = 1
    current_range = 1
    the_best_left_index = 0
    the_best_right_index = 0
    current_right_index = 0
    current_left_index = 0

    for i in range(len(candidate_indexes) - 1):
        if candidate_indexes[i] + 1 == candidate_indexes[i + 1]:
            current_range += 1
            current_right_index = i + 1
        else:
            if current_range > the_best_range:
                the_best_range = current_range
                the_best_left_index = current_left_index
                the_best_right_index = current_right_index

            current_range = 1
            current_left_index = i + 1
            current_right_index = i + 1

    # NOTE: A safeguard if we never hit else before. Consider: [1, 3, 4, 5].
    if current_range > the_best_range:
        the_best_range = current_range
        the_best_left_index = current_left_index
        the_best_right_index = current_right_index

    return candidate_indexes[(the_best_left_index + the_best_right_index) // 2]


def test():
    print(bestSeat([1, 0, 1, 0, 0, 0, 1]))
    print(bestSeat([1, 1, 1]))
    print(bestSeat([0, 0, 0]))
    print(bestSeat([1, 0, 1]))
    print(bestSeat([1, 0, 1, 1, 0, 1, 0, 0, 0]))
    print(bestSeat([1, 0, 1, 1, 0, 1, 0, 0, 0, 1]))
    print(bestSeat([1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1]))
    print(bestSeat([1, 0, 0, 1]))


if __name__ == "__main__":
    test()
