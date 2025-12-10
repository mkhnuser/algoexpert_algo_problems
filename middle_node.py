# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    node = linkedList
    slow_pointer = node
    fast_pointer = node

    # NOTE: 1 2 None.
    # 1 2 3 None.
    # 1.
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer


def middleNode(linkedList):
    # NOTE: a b c -> b c
    #       0 1 2
    #       a b c d -> c d
    #       0 1 2 3

    head = linkedList
    count = 0

    while head is not None:
        count += 1
        head = head.next

    # NOTE: We separate a number of elements from their indexes.
    middle_index = count // 2

    head = linkedList

    while head is not None and middle_index > 0:
        middle_index -= 1
        head = head.next

    return head


def test():
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    three = LinkedList(value=3)
    one.next = two
    two.next = three
    assert middleNode(one) is two


if __name__ == "__main__":
    test()
