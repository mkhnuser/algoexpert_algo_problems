class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    new_one = reverse_linked_list(linkedListOne)
    new_two = reverse_linked_list(linkedListTwo)
    sum_repr_one = sum_repr_list(new_one)
    sum_repr_two = sum_repr_list(new_two)
    summation = int(sum_repr_one) + int(sum_repr_two)
    summation_repr = str(summation)
    constructed_head = construct_list(summation_repr)
    new_constructed_head = reverse_linked_list(constructed_head)
    return new_constructed_head


def construct_list(summation_repr):
    head = LinkedList(int(summation_repr[0]))
    current = head

    for char in summation_repr[1:]:
        current.next = LinkedList(None)
        current = current.next
        current.value = int(char)

    return head


def sum_repr_list(list_):
    sum_repr = ""

    while list_ is not None:
        sum_repr += str(list_.value)
        list_ = list_.next

    return sum_repr


def reverse_linked_list(list_):
    if list_ is None:
        return None
    if list_.next is None:
        return list_

    new_head = reverse_linked_list(list_.next)
    list_.next.next = list_
    list_.next = None
    return new_head


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
