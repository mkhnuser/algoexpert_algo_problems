class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    seen = set()

    while head is not None:
        if head in seen:
            return head

        seen.add(head)
        head = head.next


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def test():
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    three = LinkedList(value=3)

    one.next = two
    two.next = three
    three.next = two

    assert findLoop(one) is two


if __name__ == "__main__":
    test()
