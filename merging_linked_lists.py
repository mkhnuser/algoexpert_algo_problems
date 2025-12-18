class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # NOTE: Example one.
    # 42 57 1 2 3
    # 1 2 3
    # Result: Node(1).
    # NOTE: Example two.
    # 1 2
    # 3 4
    # Result: None.

    node_one = linkedListOne
    node_two = linkedListTwo

    while node_one is not None:
        while node_two is not None:
            if node_one.value == node_two.value:
                return node_one

            node_two = node_two.next

        node_two = linkedListTwo
        node_one = node_one.next

    return None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    list_one_nodes = set()
    node_one = linkedListOne

    while node_one is not None:
        list_one_nodes.add(node_one)
        node_one = node_one.next

    node_two = linkedListTwo
    while node_two is not None:
        if node_two in list_one_nodes:
            return node_two
        node_two = node_two.next

    return None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # NOTE: Example one.
    # 42 57 1 2 3
    # 1 2 3
    # Result: Node(1).
    # NOTE: Example two.
    # 1 2
    # 3 4
    # Result: None.

    list_one_length = 0
    list_two_length = 0

    while linkedListOne is not None:
        linkedListOne = linkedListOne.next
        list_one_length += 1

    while linkedListTwo is not None:
        linkedListTwo = linkedListTwo.next
        list_two_length += 1

    length_difference = abs(list_one_length - list_two_length)

    list_one_pointer = linkedListOne
    list_two_pointer = linkedListTwo

    if list_one_length > list_two_length:
        while length_difference:
            list_one_pointer = list_one_pointer.next
            length_difference -= 1
    elif list_two_length > list_one_length:
        while length_difference:
            list_two_pointer = list_two_pointer.next
            length_difference -= 1

    while list_one_pointer is not None and list_two_pointer is not None:
        if list_one_pointer is list_two_pointer:
            return list_one_pointer
        list_one_pointer = list_one_pointer.next
        list_two_pointer = list_two_pointer.next
