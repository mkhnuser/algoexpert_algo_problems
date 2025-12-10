class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList

    while current_node is not None:
        next_node = current_node.next

        while next_node is not None and current_node.value == next_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = next_node

    return linkedList


def removeDuplicatesFromLinkedList(linkedList):
    # NOTE: 1 1 3 4 4 4 5 6 6 None
    # 1 3 4 5 6
    head = linkedList

    while head is not None:
        while head.next and head.next.value == head.value:
            head.next = head.next.next
        head = head.next

    return linkedList


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def test():
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    three = LinkedList(value=2)
    four = LinkedList(value=2)
    five = LinkedList(value=3)
    six = LinkedList(value=3)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    one = removeDuplicatesFromLinkedList(one)
    print_list(one)


if __name__ == "__main__":
    test()
