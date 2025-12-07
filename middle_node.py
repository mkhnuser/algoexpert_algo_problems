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


def test():
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    three = LinkedList(value=3)
    one.next = two
    two.next = three
    assert middleNode(one) is two


if __name__ == "__main__":
    test()
