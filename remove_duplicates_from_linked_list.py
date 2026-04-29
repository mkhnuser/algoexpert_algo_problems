class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    if linkedList is None:
        return None

    c = linkedList

    while c.next is not None:
        if c.value == c.next.value:
            c.next = c.next.next
        else:
            c = c.next

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
