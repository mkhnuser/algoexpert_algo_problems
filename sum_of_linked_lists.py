class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # NOTE: Create a new linked list.
    list_one_digits = ""
    one_initial_head = linkedListOne
    list_one_head_next = linkedListOne.next

    while linkedListOne is not None:
        list_one_digits += str(linkedListOne.value)

        if linkedListOne.next is None:
            one_initial_head.next = list_one_head_next
            break

        linkedListOne = linkedListOne.next

    list_one_num = int(list_one_digits[::-1])

    list_two_digits = ""
    two_initial_head = linkedListTwo
    list_two_head_next = linkedListTwo.next

    while linkedListTwo is not None:
        list_two_digits += str(linkedListTwo.value)

        if linkedListTwo.next is None:
            two_initial_head.next = list_two_head_next
            break

        linkedListTwo = linkedListTwo.next

    linkedListTwo.next = list_two_head_next
    list_two_num = int(list_two_digits[::-1])

    summation = list_one_num + list_two_num
    summation_repr = str(summation)[::-1]

    head_node = LinkedList(value=None)
    prev = head_node

    for i, char in enumerate(summation_repr):
        if i == 0:
            head_node.value = int(char)
            continue

        new_node = LinkedList(value=int(char))
        prev.next = new_node
        prev = new_node

    return head_node


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # NOTE: Example.
    # 2 4 7 1 = 1742
    # 9 4 5 = 549
    # Their sum: 2291 -> we output: 1 9 2 2 (as a new list).
    dummy_node = LinkedList(value=-1)
    prev = dummy_node
    carry = 0

    # NOTE: We need to reset the lists to their initial states.
    # After we are done.
    initial_one_head = linkedListOne
    initial_two_head = linkedListTwo
    initial_one_next = linkedListOne.next
    initial_two_next = linkedListTwo.next

    try:
        while linkedListOne is not None or linkedListTwo is not None:
            value_one = linkedListOne.value if linkedListOne else 0
            value_two = linkedListTwo.value if linkedListTwo else 0
            summation = value_one + value_two + carry
            carry, remainder = divmod(summation, 10)
            res = LinkedList(value=remainder)
            prev.next = res
            prev = res

            if linkedListOne is not None:
                linkedListOne = linkedListOne.next
            if linkedListTwo is not None:
                linkedListTwo = linkedListTwo.next

        if carry:
            prev.next = LinkedList(value=carry)

        return dummy_node.next
    finally:
        initial_one_head.next = initial_one_next
        initial_two_head.next = initial_two_next


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def test():
    one_two = LinkedList(value=2)
    one_four = LinkedList(value=4)
    one_seven = LinkedList(value=7)
    one_one = LinkedList(value=1)

    one_two.next = one_four
    one_four.next = one_seven
    one_seven.next = one_one

    two_nine = LinkedList(9)
    two_four = LinkedList(4)
    two_five = LinkedList(5)

    two_nine.next = two_four
    two_four.next = two_five

    res_list = sumOfLinkedLists(one_two, two_nine)

    print_list(res_list)


if __name__ == "__main__":
    test()
