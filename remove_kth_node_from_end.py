class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # NOTE: Count the total number of nodes in a list.
    initial_head = head
    count = 0

    while head is not None:
        count += 1
        head = head.next

    prev_node_index = count - k
    prev_node_index -= 1
    head = initial_head

    if prev_node_index == -1:
        # NOTE: head removal has been requested.
        head.value = head.next.value
        head.next = head.next.next
        return

    # NOTE: Non-head removal has been requested.

    while head is not None and prev_node_index > 0:
        head = head.next
        prev_node_index -= 1

    if head is None:
        raise Exception("Out of bound!")

    # NOTE: Assume head is now the prev_node.
    node_to_be_deleted = head.next
    node_to_be_deleted.value = None
    head.next = node_to_be_deleted.next
    node_to_be_deleted.next = None


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def test():
    # NOTE: We have at least 2 nodes as an input, and at least k nodes.
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    one.next = two
    two.next = None

    removeKthNodeFromEnd(one, 1)
    print_list(one)


if __name__ == "__main__":
    test()
