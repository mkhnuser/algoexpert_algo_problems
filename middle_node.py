class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    list_ = linkedList
    head = linkedList

    counter = 0
    while list_ is not None:
        counter += 1
        list_ = list_.next

    # NOTE: a b c -> counter = 3 -> middle_index = 1.
    # a b c d -> counter = 4. -> middle_index = 2.

    middle_index = counter // 2
    index_counter = 0
    list_ = head

    while list_ is not None:
        if index_counter == middle_index:
            return list_

        index_counter += 1
        list_ = list_.next


def test():
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    three = LinkedList(value=3)
    one.next = two
    two.next = three
    assert middleNode(one) is two


if __name__ == "__main__":
    test()
